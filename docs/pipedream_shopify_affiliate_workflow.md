# Pipedream Workflow: Auto-Populate Shopify Store with Affiliate Products

A drop-in Pipedream design (with code steps) to fetch affiliate products, clean them up, and upsert them into Shopify with organized collections and uploaded images.

## Secrets and Environment
Set these Pipedream environment variables (or use the Secret Store):
- `SHOPIFY_STORE_DOMAIN` – e.g., `mystore.myshopify.com`
- `SHOPIFY_ADMIN_TOKEN` – private Admin API access token with `write_products`, `write_product_listings`, `write_inventory`, `write_files`
- `AFFILIATE_FEED_URL` – CSV or JSON feed endpoint (e.g., CJ, Impact, ShareASale)
- Optional: `AFFILIATE_API_KEY` if your feed requires auth
- `SLACK_WEBHOOK_URL` – for summaries (optional)

## Trigger options
- **Cron**: e.g., every hour to keep the catalog fresh.
- **HTTP**: manual refresh; accept query params like `limit`, `category`, or `since` for scoped imports.

## Step-by-step outline
1. **Fetch affiliate feed**: download CSV/JSON, handle pagination, and emit a normalized array.
2. **Deduplicate & change detection**: use a Pipedream Data Store keyed by `affiliate_id` to skip unchanged products.
3. **Clean & enrich**: sanitize descriptions, generate handles, validate image URLs, derive tags/collections.
4. **Optional image rehosting**: upload images to Shopify Files to avoid hotlinking and return Shopify-hosted URLs.
5. **Upsert products**: search by SKU/handle; create or update products, variants, images, and collection assignments.
6. **Notify**: send a Slack summary with created/updated/skipped/error counts.

## Core code steps (Node.js)
Below are representative Pipedream code steps you can paste into your workflow. Adjust field names to your feed.

### 1) Fetch and normalize the feed
```javascript
import axios from "axios";
import { parse } from "csv-parse/sync";

export default async (event, steps) => {
  const url = process.env.AFFILIATE_FEED_URL;
  const headers = process.env.AFFILIATE_API_KEY ? { Authorization: `Bearer ${process.env.AFFILIATE_API_KEY}` } : {};
  const { data, headers: resHeaders } = await axios.get(url, { headers, responseType: "arraybuffer" });

  let items;
  if ((resHeaders["content-type"] || "").includes("csv")) {
    const csv = Buffer.from(data).toString("utf8");
    items = parse(csv, { columns: true, skip_empty_lines: true });
  } else {
    items = typeof data === "string" ? JSON.parse(data) : data;
  }

  const normalized = items.map((item) => ({
    affiliate_id: item.id || item.sku,
    title: item.title?.trim() || item.name,
    body_html: item.description || "",
    brand: item.brand || item.vendor,
    product_type: item.category || "Affiliate",
    price: parseFloat(item.price) || 0,
    compare_at_price: parseFloat(item.compare_at_price) || undefined,
    sku: item.sku || item.id,
    options: [item.option_name || "Size", item.option2_name || "Color"].filter(Boolean),
    variants: item.variants || [{
      sku: item.sku,
      price: parseFloat(item.price) || 0,
      option1: item.size || "Default",
      option2: item.color || undefined,
    }],
    images: (item.images || item.image_urls || []).slice(0, 5),
    tags: [item.category, item.brand, item.gender, `source:${item.source || "affiliate"}`].filter(Boolean),
    source: item.source || "affiliate",
  }));

  return normalized;
};
```

### 2) Deduplicate & change detection (Data Store)
```javascript
import crypto from "crypto";

export default async (event, steps, { $endpoints, $checkpoint }) => {
  const store = this.$checkpoint ?? {};
  const fresh = [];
  const unchanged = [];

  for (const product of steps.fetch_normalized) {
    const hash = crypto.createHash("sha256").update([
      product.title,
      product.price,
      product.images?.[0] || "",
    ].join("|"))
    .digest("hex");

    const prev = store[product.affiliate_id];
    if (prev === hash) {
      unchanged.push(product);
      continue;
    }
    store[product.affiliate_id] = hash;
    fresh.push(product);
  }

  this.$checkpoint = store;
  return { fresh, unchanged };
};
```

### 3) Optional image rehosting to Shopify Files
```javascript
import axios from "axios";

const shop = process.env.SHOPIFY_STORE_DOMAIN;
const token = process.env.SHOPIFY_ADMIN_TOKEN;

export default async (event, steps) => {
  const headers = { "X-Shopify-Access-Token": token, "Content-Type": "application/json" };
  const products = steps.dedupe.fresh;

  for (const product of products) {
    const hosted = [];
    for (const src of product.images || []) {
      try {
        const fileRes = await axios.post(`https://${shop}/admin/api/2024-07/files.json`, {
          file: { url: src }
        }, { headers });
        const url = fileRes.data?.file?.public_url || fileRes.data?.file?.url;
        if (url) hosted.push(url);
      } catch (err) {
        console.log("image upload failed", src, err.response?.data || err.message);
      }
    }
    if (hosted.length) product.images = hosted;
  }
  return products;
};
```

### 4) Upsert products in Shopify
```javascript
import axios from "axios";

const shop = process.env.SHOPIFY_STORE_DOMAIN;
const token = process.env.SHOPIFY_ADMIN_TOKEN;
const headers = { "X-Shopify-Access-Token": token, "Content-Type": "application/json" };

async function findProductIdBySku(sku) {
  const query = `query { products(first:1, query:"sku:${sku}") { edges { node { id handle } } } }`;
  const res = await axios.post(`https://${shop}/admin/api/2024-07/graphql.json`, { query }, { headers });
  return res.data.data.products.edges[0]?.node.id;
}

export default async (event, steps) => {
  const products = steps.rehost_images || steps.dedupe.fresh;
  const results = { created: 0, updated: 0, errors: [] };

  for (const product of products) {
    try {
      const existingId = await findProductIdBySku(product.sku);
      if (existingId) {
        await axios.put(`https://${shop}/admin/api/2024-07/products/${existingId.split("/").pop()}.json`, {
          product: {
            id: existingId.split("/").pop(),
            title: product.title,
            body_html: product.body_html,
            vendor: product.brand,
            product_type: product.product_type,
            tags: product.tags,
            images: (product.images || []).map((src) => ({ src })),
            variants: product.variants,
            status: "active",
          }
        }, { headers });
        results.updated++;
      } else {
        await axios.post(`https://${shop}/admin/api/2024-07/products.json`, {
          product: {
            title: product.title,
            body_html: product.body_html,
            vendor: product.brand,
            product_type: product.product_type,
            tags: product.tags,
            images: (product.images || []).map((src) => ({ src })),
            variants: product.variants,
            status: "active",
          }
        }, { headers });
        results.created++;
      }
    } catch (err) {
      results.errors.push({ sku: product.sku, message: err.response?.data || err.message });
    }
  }

  return results;
};
```

### 5) Slack summary
```javascript
import axios from "axios";

export default async (event, steps) => {
  const { created, updated, errors } = steps.upsert_products;
  if (!process.env.SLACK_WEBHOOK_URL) return "skipped";

  const text = [
    `Created: ${created}`,
    `Updated: ${updated}`,
    `Errors: ${errors.length}`,
  ].join(" | ");

  await axios.post(process.env.SLACK_WEBHOOK_URL, { text });
  return text;
};
```

## Notes and guardrails
- Start with a small `limit` and a manual HTTP trigger to validate field mapping before scheduling.
- Respect API rate limits: throttle requests (Shopify GraphQL cost-based or REST 2/s burst) and paginate feeds.
- Prefer Shopify GraphQL bulk operations for very large catalogs.
- Store additional metadata in metafields (e.g., `affiliate.id`, `affiliate.source`, `affiliate.url`) if your theme/app needs it.
- Keep a fallback draft mode: if images are missing or descriptions are empty, set `status: "draft"` to avoid low-quality listings.

This workflow gives Pipedream the code and structure needed to continuously backfill and maintain a clean, organized catalog populated from affiliate feeds.
