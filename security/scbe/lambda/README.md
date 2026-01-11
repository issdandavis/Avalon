# SCBE v2.0 - AWS Lambda Deployment

This directory contains the AWS Lambda deployment configuration and test client for the SCBE v2.0 system.

## Quick Start

```bash
# 1. Build and deploy
sam build
sam deploy --guided

# 2. Get API endpoint from output
export SCBE_API_ENDPOINT="https://your-api-id.execute-api.us-east-1.amazonaws.com/Prod"

# 3. Run tests
node test-client.js
```

## Files

- **handler.js** - Lambda function handler with dual-lane endpoints
- **test-client.js** - Test client demonstrating both patent seams
- **DEPLOYMENT_GUIDE.md** - Complete deployment documentation
- **../template.yaml** - AWS SAM template (in parent directory)

## Patent Seams

### 1. Manifold-Gated Dual-Lane Key Schedule

**Brain Lane** (Internal/Fast):
- POST `/api/brain-lane`
- Low oversight, high autonomy
- Permissive thresholds (k=5.0)
- ~15ms verification
- 4 gates

**Oversight Lane** (External/Strict):
- POST `/api/oversight-lane`
- High oversight, stricter validation
- Strict thresholds (k=2.5)
- ~42ms verification
- 6 gates with drift amplification

### 2. Trajectory + Drift-Amplified Coherence Authorization

**Verify Endpoint**:
- POST `/api/verify`
- Trajectory window validation
- Phase lock verification
- Drift-amplified coherence score
- Coherence authorization (threshold: 0.7)

## Testing

### Run All Tests

```bash
node test-client.js
```

### Test Individual Seams

```javascript
const client = require('./test-client');

// Test brain lane
await client.testBrainLane();

// Test oversight lane
await client.testOversightLane();

// Test trajectory + coherence
await client.testTrajectoryCoherence();

// Get metrics
await client.getMetrics();
```

### Manual Testing

```bash
# Brain lane
curl -X POST "$SCBE_API_ENDPOINT/api/brain-lane" \
  -H "Content-Type: application/json" \
  -d '{"payload":{"test":"data"},"context":{"device_id":"test-001","run_id":"run-123","step_no":1}}'

# Oversight lane
curl -X POST "$SCBE_API_ENDPOINT/api/oversight-lane" \
  -H "Content-Type: application/json" \
  -d '{"payload":{"test":"data"},"context":{"device_id":"test-001","run_id":"run-123","step_no":1,"waypoint":0}}'

# Metrics
curl "$SCBE_API_ENDPOINT/api/metrics"

# Health
curl "$SCBE_API_ENDPOINT/api/health"
```

## Architecture

```
                    ┌─────────────────┐
                    │   API Gateway   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Lambda Handler │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼────────┐  ┌────────▼────────┐  ┌───────▼────────┐
│   Brain Lane   │  │ Oversight Lane  │  │     Verify     │
│  (Fast/Auto)   │  │ (Strict/Valid)  │  │ (Traj+Drift)   │
└────────────────┘  └─────────────────┘  └────────────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  SCBE Pipeline  │
                    │   (6 gates)     │
                    └─────────────────┘
```

## Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete instructions.

### Prerequisites

- AWS CLI configured
- AWS SAM CLI installed
- Node.js >= 14.0.0

### Deploy

```bash
cd security/scbe
sam build
sam deploy --guided
```

### Update

```bash
sam build
sam deploy
```

### Delete

```bash
sam delete
```

## Monitoring

### View Logs

```bash
sam logs -n ScbeApiFunction --tail
```

### CloudWatch Metrics

The Lambda function automatically logs:
- Verification latency
- Gate passage rates
- Trust scores
- Rejection reasons
- Drift amplification scores

### Custom Metrics

```bash
# Get current metrics
curl "$SCBE_API_ENDPOINT/api/metrics"
```

## Performance

Expected latencies (512MB Lambda):

| Operation | Cold Start | Warm |
|-----------|-----------|------|
| Brain Lane | ~800ms | ~15ms |
| Oversight Lane | ~800ms | ~42ms |
| Verify | ~800ms | ~28ms |
| Metrics | ~800ms | ~5ms |
| Health | ~800ms | ~2ms |

## Cost

Approximate costs:
- Lambda: $0.0000002 per request
- API Gateway: $3.50 per million requests
- CloudWatch Logs: ~$0.50/GB

**10,000 test requests: < $0.01**

## Security

- HTTPS only in production
- CORS enabled (restrict for production)
- No authentication in demo (add API keys for production)
- Trust store is in-memory (use DynamoDB for production)

## Troubleshooting

### Can't connect to API

```bash
# Check endpoint
echo $SCBE_API_ENDPOINT

# Test directly
curl "$SCBE_API_ENDPOINT/api/health"
```

### Lambda timeout

Increase timeout in `../template.yaml`:

```yaml
Globals:
  Function:
    Timeout: 60
```

### View errors

```bash
sam logs -n ScbeApiFunction --tail
```

## Next Steps

1. ✅ Deploy to AWS Lambda
2. ✅ Test both patent seams
3. → Add DynamoDB persistence
4. → Add API key authentication
5. → Set up CloudWatch dashboards
6. → Add automated testing

---

For complete documentation, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
