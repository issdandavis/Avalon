# SCBE Envelope System v2.0

**Secure Chaos-Based Encryption Envelope** - Immutable security envelope for gateway → orchestrator → providers with deterministic verification and fail-to-noise protection.

## Overview

The SCBE system provides a comprehensive security framework for distributed AI/ML systems with the following features:

- **Deterministic verification** - All inputs for decryption are contained in the envelope
- **Multi-layer security gates** - 6 independent verification stages
- **Fail-to-noise** - Failed requests return deterministic noise instead of errors
- **Swarm trust** - Automatic trust decay and agent exclusion
- **No timing oracles** - Constant-time error responses
- **Post-quantum ready** - Uses ML-KEM-768 and ML-DSA-65

## Quick Start

### Installation

```bash
# In your project root
npm install ./security/scbe
```

Or copy the `security/scbe` directory to your project.

### Basic Usage

```javascript
const scbe = require('./security/scbe');

// Create an envelope
const envelope = scbe.buildEnvelope({
  ctx: {
    ts: Math.floor(Date.now() / 1000),
    device_id: 'user_device_123',
    threat_level: 2,
    entropy: 0.5,
    server_load: 0.4,
    stability: 0.9
  },
  intent: {
    primary: 'sil\'kor',
    modifier: 'nav\'een',
    harmonic: 3,
    phase_deg: 45
  },
  trajectory: {
    epoch: Math.floor(Date.now() / 1000) - 1000,
    period_s: 3600,
    slot_id: 'daily-08-12-16-20',
    waypoint: 1
  },
  aad: {
    route_hint: 'openai',
    run_id: 'run_xxx',
    step_no: 7
  },
  crypto: {
    cipher_b64: encryptedPayload.toString('base64')
  }
});

// Verify an envelope
const config = {
  currentTs: Math.floor(Date.now() / 1000),
  energyConfig: {
    mean: 1.0,
    std: 0.3,
    k: 3.0,
    epsilon: 0.1
  },
  trustStore: new scbe.TrustStore()
};

const result = await scbe.runVerificationPipeline(envelope, config);

if (result.success) {
  // Process envelope
  console.log('Verification passed');
} else {
  // Return noise envelope
  console.log('Verification failed:', result.reason);
  return result.noiseEnvelope;
}
```

## Envelope Structure

```json
{
  "ver": "scbe-2.0",
  "ctx": {
    "ts": 1736434000,
    "device_id": "user_device_5a2k9",
    "threat_level": 3,
    "entropy": 0.72,
    "server_load": 0.45,
    "stability": 0.89
  },
  "intent": {
    "primary": "sil'kor",
    "modifier": "nav'een",
    "harmonic": 3,
    "phase_deg": 45
  },
  "trajectory": {
    "epoch": 1736380800,
    "period_s": 3600,
    "slot_id": "daily-08-12-16-20",
    "waypoint": 1
  },
  "aad": {
    "route_hint": "openai",
    "run_id": "run_xxx",
    "step_no": 7
  },
  "commit": {
    "ctx_sha256": "...",
    "intent_sha256": "...",
    "traj_sha256": "...",
    "aad_sha256": "..."
  },
  "crypto": {
    "kem": "ML-KEM-768",
    "sig": "ML-DSA-65",
    "h": { "d": 4, "R": 1.5, "H": 1.5**16, "n_iter": 6500 },
    "salt_q_b64": "...",
    "cipher_b64": "..."
  },
  "sig": {
    "orchestrator_sig_b64": "...",
    "provider_sig_b64": null
  }
}
```

## Verification Pipeline

The pipeline runs 6 gates in order (cheap → expensive):

### Gate 1: Schema Validation
- Validates envelope structure
- Clamps `[0,1]` floats
- Verifies all commit hashes match recomputed values

### Gate 2: Fractal Gate
- Computes Julia set iterations for `z0(ctx)` and `c(intent)`
- Rejects if iterations ≤ threshold (chaos-based rejection)
- Cheap rejection for invalid requests

### Gate 3: Intent Policy
- Checks if `(primary, modifier, harmonic)` is allowed for provider
- Prevents cross-domain operations
- Configurable per-provider policies

### Gate 4: Trajectory & Phase Lock
- Validates time window against slot policy
- Compares `phase_deg` with computed phase from trajectory
- Detects replay attacks and clock drift

### Gate 5: Neural Behavior Energy
- Computes energy `E(ctx_norm)` from normalized context
- Rejects if `E > μ + kσ` (anomaly detection)
- Detects gradient margin proximity (boundary attackers)

### Gate 6: Swarm Trust
- Requires provider trust `τ ≥ 0.3`
- Requires swarm entropy `H ≥ 0.5`
- Auto-excludes low-trust providers

### Gate 7: Cryptographic Verification
- Verifies orchestrator signature
- KEM decapsulation
- Chaos diffusion decryption

## Fail-to-Noise

All rejection paths return deterministic noise:

```javascript
// On any gate failure
const noise = scbe.generateDeterministicNoise(
  envelope.commit.ctx_sha256,
  envelope.crypto.salt_q_b64,
  4096,  // min size
  8192   // max size
);

const noiseEnvelope = scbe.createNoiseResponse(envelope, noise);
```

**Benefits:**
- No timing oracles (constant response size bands)
- No information leakage about failure reason
- Deterministic for testing/auditing

## Trust Management

```javascript
const trustStore = new scbe.TrustStore();

// Initialize providers
trustStore.initialize('openai', 0.8);
trustStore.initialize('anthropic', 0.8);

// Update trust based on behavior
const validity = scbe.computeValidity({
  neuralPassed: true,
  coherence: 0.9,
  deviationPenalty: 0.1
});

trustStore.updateTrust('openai', validity);

// Check exclusion
if (trustStore.shouldExclude('provider')) {
  console.log('Provider excluded due to low trust');
}

// Get metrics
console.log('Average trust:', trustStore.getAverageTrust());
console.log('Swarm entropy:', trustStore.getSwarmEntropy());
```

## Observability

### Metrics

```javascript
const scbe = require('./security/scbe');

// Record events
scbe.recordRejection('fractal');
scbe.recordPhaseSkew(12);
scbe.updateSwarmMetrics(trustStore);
scbe.recordProviderCoherence('openai', 0.95);

// Get summary
const summary = scbe.getMetricsSummary();
console.log('Phase skew p95:', summary.phase_skew_p95);
console.log('Swarm trust avg:', summary.swarm_trust_avg);

// Check alerts
const alerts = scbe.checkAlerts({
  swarm_trust_avg: 0.5,
  gft_score: 0.8,
  phase_skew_p95: 30
});

alerts.forEach(alert => {
  console.log(`[${alert.severity}] ${alert.message}`);
});
```

### Key Metrics

- `scbe.verify.reject_total{reason}` - Rejection counter by reason
- `scbe.phase.skew_deg` - Phase skew histogram
- `swarm.trust.avg` - Average swarm trust
- `swarm.trust{agent}` - Per-agent trust
- `gft.rightshift.score` - Spectral anomaly score
- `provider.coherence{provider}` - Provider coherence score

## Security Scenarios

The system protects against 5 critical attack scenarios:

### 1. API Key Theft
**Attack:** Stolen credentials used from different context  
**Defense:** 3 gates (commit hash, neural energy, swarm trust)  
**Test:** `npm test -- --grep "Key Theft"`

### 2. Prompt Injection
**Attack:** Malicious intent in wrong time slot  
**Defense:** Intent policy + trajectory gate  
**Test:** `npm test -- --grep "Confused Deputy"`

### 3. Compromised Provider
**Attack:** Provider behaving maliciously  
**Defense:** Coherence tracking + trust decay → auto-exclude  
**Test:** `npm test -- --grep "Provider Compromise"`

### 4. Agent Collusion
**Attack:** Multiple agents coordinating attacks  
**Defense:** Spectral analysis + centroid deviation → trust decay  
**Test:** `npm test -- --grep "Collusion"`

### 5. Replay Attacks
**Attack:** Reusing valid envelopes later  
**Defense:** Phase lock + trajectory window  
**Test:** `npm test -- --grep "Replay"`

## Testing

Run all security tests:

```bash
cd security/scbe
node tests/security-tests.js
```

Expected output:
```
======================================
SCBE Security Test Suite
======================================

=== Test 1: Replay Attack ===
✓ Replay attack correctly rejected

=== Test 2: Confused Deputy ===
✓ Confused deputy attack correctly rejected

=== Test 3: Low-grade Collusion ===
✓ Colluding agents correctly excluded

=== Test 4: Key Theft ===
✓ Key theft correctly rejected

=== Test 5: Provider Compromise ===
✓ Compromised provider correctly excluded

======================================
Test Results Summary
======================================
✓ ALL TESTS PASSED
```

## Rollout Plan

### Week 1: Foundation
- [ ] Deploy envelope schema + validation
- [ ] Implement fail-to-noise (no crypto yet)
- [ ] Wire basic metrics

### Week 2: Policy Gates
- [ ] Add intent/trajectory/phase checks
- [ ] Configure alert thresholds
- [ ] Test with synthetic traffic

### Week 3: Behavior Gates
- [ ] Enable neural energy gate (permissive)
- [ ] Observe false positive rate
- [ ] Tune thresholds

### Week 4: Trust System
- [ ] Enable swarm trust decay
- [ ] Shadow mode for 3 days
- [ ] Enforce auto-exclusion

### Week 5: Post-Quantum Crypto
- [ ] Flip to ML-KEM/ML-DSA
- [ ] Validate production paths
- [ ] Performance testing

### Week 6: Provider Integration
- [ ] Add provider return signatures
- [ ] Full decrypt path
- [ ] End-to-end validation

## Configuration

### Minimal Config

```javascript
const config = {
  currentTs: Math.floor(Date.now() / 1000),
  energyConfig: {
    mean: 1.0,
    std: 0.3,
    k: 3.0,
    epsilon: 0.1
  }
};
```

### Full Config

```javascript
const config = {
  currentTs: Math.floor(Date.now() / 1000),
  
  intentPolicy: {
    providers: {
      openai: {
        allowed_intents: [
          'sil\'kor:nav\'een',
          'sil\'kor:keth\'ara'
        ]
      },
      anthropic: {
        allowed_intents: [
          'sil\'kor:nav\'een'
        ]
      }
    }
  },
  
  energyConfig: {
    mean: 1.0,
    std: 0.3,
    k: 3.0,
    epsilon: 0.1,
    weights: [1.0, 0.8, 0.6, 1.2]
  },
  
  trustStore: trustStore
};
```

## API Reference

### Core Functions

#### `buildEnvelope(params)`
Creates a valid SCBE envelope with automatic commit hash generation.

**Parameters:**
- `params.ctx` - Context object
- `params.intent` - Intent object
- `params.trajectory` - Trajectory object
- `params.aad` - Additional Authenticated Data
- `params.crypto` - Crypto configuration

**Returns:** Validated envelope object

#### `runVerificationPipeline(envelope, config)`
Runs complete verification pipeline through all gates.

**Parameters:**
- `envelope` - Envelope to verify
- `config` - Verification configuration

**Returns:** Promise resolving to verification result with noise envelope on failure

#### `TrustStore`
Manages trust scores with decay and auto-exclusion.

**Methods:**
- `initialize(provider, trust)` - Initialize provider
- `getTrust(provider)` - Get current trust
- `updateTrust(provider, validity)` - Update based on behavior
- `shouldExclude(provider)` - Check exclusion status
- `getSwarmEntropy()` - Get diversity metric
- `getAverageTrust()` - Get average trust

### Utilities

#### `canonicalize(obj)`
Deterministically stringify object with sorted keys.

#### `sha256Object(obj)`
Compute SHA-256 of canonicalized object.

#### `generateDeterministicNoise(ctx_sha256, salt_q_b64, minSize, maxSize)`
Generate deterministic noise for fail-to-noise responses.

#### `calculateCurrentPhase(trajectory, currentTs)`
Calculate phase angle from trajectory parameters.

## Security Considerations

### Determinism Requirements
- **NO** `Math.random()` in context or KDF inputs
- Use GPS/NTP with monotonic guard for timestamps
- Record `clock_source` and skew metrics

### Key Management
- Store secrets in KMS or seal with app master key
- Rotate keys quarterly
- Never log raw decrypted payloads

### Constant-Time Requirements
- Normalize error response sizes into bands (e.g., 8KB buckets)
- Add deterministic delay jitter from `ctx_sha256`
- Use same codepath for all rejection reasons

### Provider Integration
- Require providers echo AAD and sign results
- Bind responses to intents (prevents swapping)
- Track coherence with historical "honest" basis

## Architecture

```
Gateway
   ├─> Build envelope with commit hashes
   ├─> Sign with orchestrator key
   └─> Send to orchestrator

Orchestrator
   ├─> Gate 1: Schema validation
   ├─> Gate 2: Fractal gate
   ├─> Gate 3: Intent policy
   ├─> Gate 4: Trajectory & phase
   ├─> Gate 5: Neural energy
   ├─> Gate 6: Swarm trust
   ├─> Gate 7: Crypto verification
   ├─> Route to provider (if passed)
   └─> Return noise (if failed)

Provider
   ├─> Process request
   ├─> Sign response
   └─> Return signed envelope

Orchestrator
   ├─> Verify provider signature
   ├─> Update trust score
   └─> Return to gateway
```

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
- GitHub Issues: [Create an issue](https://github.com/issdandavis/aethromoor-novel/issues)
- Documentation: This README
- Tests: `security/scbe/tests/`

## Version History

### v2.0.0 (Current)
- Initial SCBE implementation
- 6-gate verification pipeline
- Fail-to-noise protection
- Trust management system
- Comprehensive test suite
- Full documentation
