# SCBE v2.0 - AWS Lambda Deployment Guide

## Overview

This guide shows how to deploy the SCBE v2.0 system to AWS Lambda and test the two patent seams:
1. **Manifold-gated dual-lane key schedule** (brain vs oversight lanes)
2. **Trajectory + drift-amplified coherence authorization**

## Prerequisites

- AWS Account with appropriate permissions
- AWS CLI configured (`aws configure`)
- AWS SAM CLI installed ([install guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))
- Node.js >= 14.0.0

## Quick Start

### 1. Install SAM CLI (if not installed)

```bash
# macOS
brew install aws-sam-cli

# Linux
pip install aws-sam-cli

# Windows
choco install aws-sam-cli
```

### 2. Deploy to AWS Lambda

```bash
cd security/scbe

# Build the Lambda function
sam build

# Deploy (first time - will create CloudFormation stack)
sam deploy --guided

# Follow the prompts:
# - Stack Name: scbe-v2-demo
# - AWS Region: us-east-1 (or your preferred region)
# - Confirm changes: Y
# - Allow SAM CLI IAM role creation: Y
# - Save arguments to config: Y

# After first deployment, you can just run:
sam deploy
```

### 3. Get the API Endpoint

After deployment, SAM will output the API endpoint URL:

```
CloudFormation outputs from deployed stack
-------------------------------------------------------------------------
Outputs                                                                          
-------------------------------------------------------------------------
Key                 ScbeApi                                                      
Description         API Gateway endpoint URL for SCBE API                       
Value               https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/Prod/
-------------------------------------------------------------------------
```

Save this URL - you'll need it for testing.

### 4. Test the API

```bash
# Set your API endpoint
export SCBE_API_ENDPOINT="https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/Prod"

# Make the test client executable
chmod +x lambda/test-client.js

# Run all tests
node lambda/test-client.js
```

## API Endpoints

### Patent Seam 1: Manifold-Gated Dual-Lane

#### Brain Lane (Internal/Fast)
**POST** `/api/brain-lane`

Low oversight, high autonomy, optimized for speed.

```bash
curl -X POST "$SCBE_API_ENDPOINT/api/brain-lane" \
  -H "Content-Type: application/json" \
  -d '{
    "payload": {
      "operation": "analyze",
      "data": { "input": "test data" }
    },
    "context": {
      "device_id": "brain-test-001",
      "run_id": "brain-run-123",
      "step_no": 1
    }
  }'
```

**Response:**
```json
{
  "success": true,
  "lane": "brain",
  "envelope_id": "c5b6c3bfa6b7f121",
  "verification_ms": 15,
  "gates_passed": 4,
  "trust_score": "0.920",
  "message": "Brain lane processed: fast autonomous execution"
}
```

#### Oversight Lane (External/Strict)
**POST** `/api/oversight-lane`

High oversight, stricter validation, coherence tracking.

```bash
curl -X POST "$SCBE_API_ENDPOINT/api/oversight-lane" \
  -H "Content-Type: application/json" \
  -d '{
    "payload": {
      "operation": "validate",
      "data": { "input": "test data" }
    },
    "context": {
      "device_id": "oversight-test-001",
      "run_id": "oversight-run-123",
      "step_no": 1,
      "waypoint": 0
    }
  }'
```

**Response:**
```json
{
  "success": true,
  "lane": "oversight",
  "envelope_id": "f0a7387642e37c2e",
  "verification_ms": 42,
  "gates_passed": 6,
  "trust_score": "0.875",
  "drift_amplified": {
    "phase_skew_deg": 8.5,
    "energy_margin": 0.654,
    "coherence": 0.812,
    "amplified": true
  },
  "message": "Oversight lane processed: validated with drift amplification"
}
```

### Patent Seam 2: Trajectory + Drift-Amplified Coherence

**POST** `/api/verify`

Generic verification demonstrating trajectory validation and drift-amplified coherence authorization.

```bash
# First, create an envelope (can use Node.js or test client)
node -e "
const scbe = require('./index');
const envelope = scbe.buildEnvelope({
  ctx: {
    ts: Math.floor(Date.now() / 1000),
    device_id: 'test-001',
    threat_level: 3,
    entropy: 0.5,
    server_load: 0.4,
    stability: 0.85
  },
  intent: {
    primary: 'sil\\'kor',
    modifier: 'nav\\'een',
    harmonic: 3,
    phase_deg: 45
  },
  trajectory: {
    epoch: Math.floor(Date.now() / 1000) - 600,
    period_s: 3600,
    slot_id: 'test-slot',
    waypoint: 0
  },
  aad: {
    route_hint: 'test-provider',
    run_id: 'test-run-123',
    step_no: 1
  },
  crypto: {
    cipher_b64: Buffer.from(JSON.stringify({ test: 'data' })).toString('base64')
  }
});
console.log(JSON.stringify({ envelope }, null, 2));
" > envelope.json

# Send to verify endpoint
curl -X POST "$SCBE_API_ENDPOINT/api/verify" \
  -H "Content-Type: application/json" \
  -d @envelope.json
```

**Response:**
```json
{
  "success": true,
  "verification_ms": 28,
  "gates": [
    { "gate": "schema", "passed": true },
    { "gate": "fractal", "passed": true },
    { "gate": "trajectory", "passed": true },
    { "gate": "neural", "passed": true }
  ],
  "trajectory_valid": true,
  "drift_amplification": {
    "phase_skew_deg": 5.2,
    "energy_margin": 0.742,
    "coherence": 0.893,
    "amplified": true
  },
  "coherence_authorized": true
}
```

### Monitoring Endpoints

#### Metrics
**GET** `/api/metrics`

```bash
curl "$SCBE_API_ENDPOINT/api/metrics"
```

**Response:**
```json
{
  "summary": {
    "phase_skew_p50": 8.5,
    "phase_skew_p95": 15.2,
    "swarm_trust_avg": 0.875,
    "rejections": {
      "fractal": 0,
      "intent": 0,
      "trajectory": 2,
      "neural": 1
    }
  },
  "trust_scores": {
    "brain-lane": "0.920",
    "oversight-lane": "0.875",
    "openai": "0.800",
    "anthropic": "0.800"
  },
  "swarm_entropy": "0.894"
}
```

#### Health Check
**GET** `/api/health`

```bash
curl "$SCBE_API_ENDPOINT/api/health"
```

## Files Required for Deployment

The following files are needed and automatically included:

```
security/scbe/
├── template.yaml              # SAM/CloudFormation template
├── lambda/
│   ├── handler.js             # Lambda function handler
│   └── test-client.js         # Test client
├── index.js                   # SCBE main module
├── package.json               # Package definition
├── core/                      # Core modules (3 files)
├── verification/              # Verification modules (2 files)
└── utils/                     # Utility modules (1 file)
```

**Total:** 10 files (handler + 9 SCBE core files)

All dependencies are bundled - no external packages needed!

## Local Testing (Optional)

You can test locally before deploying to AWS:

```bash
# Install SAM local dependencies
npm install

# Start local API
sam local start-api

# In another terminal, test with local endpoint
export SCBE_API_ENDPOINT="http://localhost:3000"
node lambda/test-client.js
```

## Deployment Commands Reference

```bash
# Build Lambda package
sam build

# Deploy to AWS
sam deploy

# Deploy to specific region
sam deploy --region us-west-2

# View logs
sam logs -n ScbeApiFunction --tail

# Delete deployment
sam delete
```

## Testing the Patent Seams

### Test 1: Manifold-Gated Dual-Lane

Demonstrates the difference between brain lane (fast/autonomous) and oversight lane (strict/validated):

```bash
# Run dual-lane comparison test
node lambda/test-client.js

# Expected output:
# Comparison Results:
# ─────────────────────────────────────────────
#                     Brain Lane    Oversight Lane
# ─────────────────────────────────────────────
# Success:            ✓            ✓
# Verification (ms):  15           42
# Trust Score:        0.920        0.875
# Gates Passed:       4            6
```

**Key Differences:**
- **Brain lane**: 4 gates (permissive), ~15ms, higher trust
- **Oversight lane**: 6 gates (strict), ~42ms, coherence tracking

### Test 2: Trajectory + Drift-Amplified Coherence

Demonstrates trajectory validation and coherence authorization:

```bash
# Test trajectory coherence
node -e "
const { testTrajectoryCoherence } = require('./lambda/test-client');
testTrajectoryCoherence();
"

# Expected output:
# ✓ Trajectory + coherence: PASS
#   - Trajectory valid: YES
#   - Coherence authorized: YES
#   - Phase skew: 5.20°
#   - Energy margin: 0.742
#   - Coherence score: 0.893
#   - Amplified: YES
```

**Key Metrics:**
- **Trajectory valid**: Time window check passed
- **Phase skew**: < 15° tolerance
- **Coherence**: Derived from phase skew + energy margin
- **Amplified**: Coherence > 0.7 threshold

## Performance Metrics

Expected performance in AWS Lambda (512MB memory):

| Endpoint | Cold Start | Warm | Gates |
|----------|-----------|------|-------|
| Brain Lane | ~800ms | ~15ms | 4 |
| Oversight Lane | ~800ms | ~42ms | 6 |
| Verify | ~800ms | ~28ms | 4-6 |

## Troubleshooting

### Deployment Fails

```bash
# Check CloudFormation stack
aws cloudformation describe-stack-events \
  --stack-name scbe-v2-demo \
  --region us-east-1

# View logs
sam logs -n ScbeApiFunction --tail
```

### Test Client Can't Connect

```bash
# Verify endpoint is correct
echo $SCBE_API_ENDPOINT

# Test health endpoint directly
curl "$SCBE_API_ENDPOINT/api/health"

# Check if API Gateway is accessible
curl "$SCBE_API_ENDPOINT/"
```

### Lambda Timeout

If verification takes too long, increase timeout in `template.yaml`:

```yaml
Globals:
  Function:
    Timeout: 60  # Increase from 30 to 60 seconds
```

Then redeploy: `sam deploy`

## Cost Estimate

Approximate AWS costs for testing:

- **Lambda**: $0.0000002 per request (first 1M free)
- **API Gateway**: $3.50 per million requests (first 1M free)
- **CloudWatch Logs**: ~$0.50/GB ingested

**Expected cost for 10,000 test requests: < $0.01**

## Next Steps

1. ✅ Deploy to AWS Lambda
2. ✅ Test dual-lane endpoints
3. ✅ Verify trajectory + coherence
4. → Add DynamoDB for trust store persistence
5. → Add CloudWatch dashboards
6. → Set up automated testing

## Support

- **API Documentation**: `curl $SCBE_API_ENDPOINT/`
- **Health Check**: `curl $SCBE_API_ENDPOINT/api/health`
- **Metrics**: `curl $SCBE_API_ENDPOINT/api/metrics`

## Security Notes

- All endpoints use HTTPS in production
- CORS enabled for testing (restrict in production)
- No authentication required for demo (add API keys for production)
- Trust scores persist in-memory (use DynamoDB for production)

---

**Ready to deploy!** Run `sam build && sam deploy --guided` to get started.
