# SCBE Implementation Guide

## Overview

This guide provides step-by-step instructions for implementing the SCBE (Secure Chaos-Based Encryption) envelope system in your architecture.

## Architecture Components

```
┌─────────────┐
│   Gateway   │  Creates envelopes, gathers context
└──────┬──────┘
       │
       ▼
┌─────────────┐
│Orchestrator │  Verifies through 6 gates, routes
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Provider   │  Processes, signs response
└─────────────┘
```

## Phase 1: Gateway Integration (Week 1)

### 1.1 Install SCBE Module

```bash
# Copy the SCBE module to your project
cp -r security/scbe /path/to/your/project/

# Or install as npm package
cd security/scbe && npm pack
cd /path/to/your/project && npm install /path/to/scbe-envelope-2.0.0.tgz
```

### 1.2 Implement Context Collection

**Key Rule:** NO randomness in context. All values must be deterministic or derived.

```javascript
const scbe = require('./scbe');

function gatherContext(request) {
  return {
    // Use seconds, not milliseconds
    ts: Math.floor(Date.now() / 1000),
    
    // Device identifier from request
    device_id: request.deviceId || request.headers['x-device-id'],
    
    // Threat level from security scanner (0-10)
    threat_level: securityScanner.getThreatLevel(request),
    
    // Deterministic entropy (NOT Math.random())
    // Example: Shannon entropy of recent inter-arrival times
    entropy: calculateEntropyMetric(request),
    
    // Current server load [0,1]
    server_load: process.cpuUsage().system / 1000000000,
    
    // System stability metric [0,1]
    stability: systemHealth.getStabilityScore()
  };
}

function calculateEntropyMetric(request) {
  // Example: Normalized Shannon entropy
  const recentTimestamps = getRecentRequestTimestamps();
  const intervals = calculateIntervals(recentTimestamps);
  const entropy = shannonEntropy(intervals);
  return Math.max(0, Math.min(1, entropy / Math.log2(intervals.length)));
}
```

### 1.3 Create Envelope Builder

```javascript
function buildRequestEnvelope(request, sensitivePayload) {
  const ctx = gatherContext(request);
  
  const intent = {
    primary: request.operation || 'sil\'kor',
    modifier: request.modifier || 'nav\'een',
    harmonic: request.priority || 3,
    phase_deg: calculatePhase(request) // Based on scheduled time
  };
  
  const trajectory = {
    epoch: getCurrentPolicyEpoch(),
    period_s: 3600,  // 1 hour windows
    slot_id: getCurrentSlotId(),
    waypoint: request.step || 0
  };
  
  const aad = {
    route_hint: request.provider || 'openai',
    run_id: request.runId,
    step_no: request.stepNo || 0
  };
  
  // Encrypt payload (use your encryption system)
  const cipher_b64 = encryptPayload(sensitivePayload).toString('base64');
  
  return scbe.buildEnvelope({
    ctx,
    intent,
    trajectory,
    aad,
    crypto: { cipher_b64 }
  });
}
```

### 1.4 Add Envelope Validation

```javascript
async function sendToOrchestrator(envelope) {
  // Validate before sending
  try {
    scbe.validateEnvelope(envelope);
  } catch (error) {
    throw new Error(`Invalid envelope: ${error.message}`);
  }
  
  // Sign envelope (use your signing system)
  const signature = await signEnvelope(envelope);
  const signedEnvelope = scbe.addOrchestratorSignature(envelope, signature);
  
  // Send to orchestrator
  return await httpClient.post('/orchestrator/verify', signedEnvelope);
}
```

## Phase 2: Orchestrator Integration (Week 2-3)

### 2.1 Initialize Trust Store

```javascript
const scbe = require('./scbe');

// Global trust store (persist to database)
const trustStore = new scbe.TrustStore();

// Initialize known providers
trustStore.initialize('openai', 0.8);
trustStore.initialize('anthropic', 0.8);
trustStore.initialize('cohere', 0.7);

// Load from persistence
function loadTrustStore() {
  const state = database.getTrustStoreState();
  if (state) {
    trustStore.import(state);
  }
}

// Save periodically
setInterval(() => {
  database.saveTrustStoreState(trustStore.export());
}, 60000); // Every minute
```

### 2.2 Configure Verification Pipeline

```javascript
function getVerificationConfig() {
  return {
    currentTs: Math.floor(Date.now() / 1000),
    
    // Intent policy (who can do what)
    intentPolicy: {
      providers: {
        openai: {
          allowed_intents: [
            'sil\'kor:nav\'een',
            'sil\'kor:keth\'ara',
            'terra\'bind:nav\'een'
          ]
        },
        anthropic: {
          allowed_intents: [
            'sil\'kor:nav\'een'
          ]
        }
      }
    },
    
    // Neural energy thresholds
    energyConfig: {
      mean: 1.0,
      std: 0.3,
      k: 3.0,  // Start permissive, tighten later
      epsilon: 0.1
    },
    
    // Trust store
    trustStore
  };
}
```

### 2.3 Implement Verification Endpoint

```javascript
app.post('/orchestrator/verify', async (req, res) => {
  const envelope = req.body;
  const startTime = Date.now();
  
  try {
    // Run verification pipeline
    const config = getVerificationConfig();
    const result = await scbe.runVerificationPipeline(envelope, config);
    
    // Record metrics
    const duration = Date.now() - startTime;
    scbe.recordVerificationLatency(duration);
    
    if (result.success) {
      // Verification passed - route to provider
      scbe.recordEnvelopeProcessed(true);
      
      const response = await routeToProvider(envelope);
      
      // Update trust
      const validity = scbe.computeValidity({
        neuralPassed: true,
        coherence: calculateCoherence(response),
        deviationPenalty: calculateDeviation(response)
      });
      trustStore.updateTrust(envelope.aad.route_hint, validity);
      
      res.json(response);
      
    } else {
      // Verification failed - return noise
      scbe.recordRejection(result.reason);
      scbe.recordEnvelopeProcessed(false);
      
      // Add deterministic delay
      const delay = scbe.computeDeterministicDelay(
        envelope.commit.ctx_sha256,
        50,  // base delay ms
        50   // jitter ms
      );
      await sleep(delay);
      
      // Return noise envelope
      res.json(result.noiseEnvelope);
    }
    
  } catch (error) {
    // Return noise on error too (fail-to-noise)
    const noiseEnvelope = scbe.generateNoiseEnvelope(envelope);
    res.json(noiseEnvelope);
  }
});
```

### 2.4 Implement Provider Routing

```javascript
async function routeToProvider(envelope) {
  const provider = envelope.aad.route_hint;
  
  // Check trust before routing
  if (trustStore.shouldExclude(provider)) {
    throw new Error(`Provider ${provider} is excluded due to low trust`);
  }
  
  // Get provider endpoint
  const endpoint = providerRegistry.getEndpoint(provider);
  
  // Send envelope to provider
  const response = await httpClient.post(endpoint, envelope);
  
  // Verify provider signature
  if (!response.sig.provider_sig_b64) {
    throw new Error('Missing provider signature');
  }
  
  // Verify AAD binding (prevents response swapping)
  const expectedAadHash = scbe.sha256Object(envelope.aad);
  if (response.commit.aad_sha256 !== expectedAadHash) {
    throw new Error('AAD mismatch - response swapping detected');
  }
  
  return response;
}
```

## Phase 3: Observability (Week 3)

### 3.1 Export Metrics

```javascript
// Prometheus-style metrics endpoint
app.get('/metrics', (req, res) => {
  const metrics = scbe.metrics.export();
  
  // Convert to Prometheus format
  const output = [];
  
  // Counters
  for (const [key, value] of Object.entries(metrics.counters)) {
    output.push(`${key} ${value}`);
  }
  
  // Gauges
  for (const [key, value] of Object.entries(metrics.gauges)) {
    output.push(`${key} ${value}`);
  }
  
  res.type('text/plain').send(output.join('\n'));
});
```

### 3.2 Configure Alerts

```javascript
// Check for alert conditions every minute
setInterval(() => {
  const alerts = scbe.checkAlerts({
    swarm_trust_avg: 0.5,    // Alert if below 0.5
    gft_score: 0.8,          // Alert if above 0.8
    phase_skew_p95: 30       // Alert if above 30 degrees
  });
  
  alerts.forEach(alert => {
    if (alert.severity === 'critical') {
      pagerDuty.alert(alert);
    } else {
      slack.notify(alert);
    }
  });
}, 60000);
```

### 3.3 Dashboard Queries

```prometheus
# Rejection rate by reason
rate(scbe_verify_reject_total[5m])

# Average swarm trust
swarm_trust_avg

# Phase skew percentiles
histogram_quantile(0.95, scbe_phase_skew_deg)

# Verification latency
histogram_quantile(0.95, scbe_verify_duration_ms)
```

## Phase 4: Trust Maintenance (Week 4)

### 4.1 Implement Coherence Tracking

```javascript
class CoherenceTracker {
  constructor() {
    this.baselines = new Map(); // provider -> historical vectors
  }
  
  updateBaseline(provider, outputVector) {
    if (!this.baselines.has(provider)) {
      this.baselines.set(provider, []);
    }
    
    const baseline = this.baselines.get(provider);
    baseline.push(outputVector);
    
    // Keep last 100 outputs
    if (baseline.length > 100) {
      baseline.shift();
    }
  }
  
  calculateCoherence(provider, outputVector) {
    const baseline = this.baselines.get(provider);
    if (!baseline || baseline.length === 0) {
      return 1.0; // No baseline yet
    }
    
    // Compute cosine similarity with average baseline
    const avgBaseline = this.averageVectors(baseline);
    return this.cosineSimilarity(outputVector, avgBaseline);
  }
  
  cosineSimilarity(v1, v2) {
    const dot = v1.reduce((sum, val, i) => sum + val * v2[i], 0);
    const mag1 = Math.sqrt(v1.reduce((sum, val) => sum + val * val, 0));
    const mag2 = Math.sqrt(v2.reduce((sum, val) => sum + val * val, 0));
    return dot / (mag1 * mag2);
  }
  
  averageVectors(vectors) {
    const sum = new Array(vectors[0].length).fill(0);
    vectors.forEach(v => {
      v.forEach((val, i) => { sum[i] += val; });
    });
    return sum.map(val => val / vectors.length);
  }
}

const coherenceTracker = new CoherenceTracker();
```

### 4.2 Update Trust Based on Coherence

```javascript
async function updateProviderTrust(provider, response) {
  // Extract output vector (e.g., embedding of response)
  const outputVector = await extractOutputVector(response);
  
  // Calculate coherence
  const coherence = coherenceTracker.calculateCoherence(provider, outputVector);
  scbe.recordProviderCoherence(provider, coherence);
  
  // Update baseline if coherent
  if (coherence > 0.7) {
    coherenceTracker.updateBaseline(provider, outputVector);
  }
  
  // Compute validity
  const validity = scbe.computeValidity({
    neuralPassed: true,
    coherence,
    deviationPenalty: calculateDeviationPenalty(response)
  });
  
  // Update trust
  trustStore.updateTrust(provider, validity);
  
  // Check for auto-exclusion
  if (trustStore.shouldExclude(provider)) {
    logger.warn(`Provider ${provider} auto-excluded (trust=${trustStore.getTrust(provider).toFixed(3)})`);
    alerting.notify(`Provider ${provider} excluded`, 'warning');
  }
}
```

### 4.3 Global Trust Decay

```javascript
// Apply global decay daily (simulates natural erosion)
const schedule = require('node-schedule');

schedule.scheduleJob('0 0 * * *', () => {
  trustStore.applyGlobalDecay(0.95);
  logger.info('Applied global trust decay');
  
  // Update metrics
  scbe.updateSwarmMetrics(trustStore);
});
```

## Phase 5: Post-Quantum Crypto (Week 5)

### 5.1 Key Generation

```javascript
// Use a PQC library like liboqs or kyber-crystals
const { MLKem768 } = require('ml-kem');
const { MLDsa65 } = require('ml-dsa');

// Generate orchestrator keys
const kemKeys = MLKem768.generateKeyPair();
const sigKeys = MLDsa65.generateKeyPair();

// Store securely (KMS or sealed storage)
await kms.storeKey('orchestrator-kem-private', kemKeys.privateKey);
await kms.storeKey('orchestrator-sig-private', sigKeys.privateKey);

// Distribute public keys
distributePubKey('orchestrator-kem-public', kemKeys.publicKey);
distributePubKey('orchestrator-sig-public', sigKeys.publicKey);
```

### 5.2 Encryption (Gateway)

```javascript
async function encryptPayload(payload) {
  // Load provider's KEM public key
  const providerPubKey = await kms.getKey('provider-kem-public');
  
  // KEM encapsulation
  const { ciphertext: kemCipher, sharedSecret } = MLKem768.encapsulate(providerPubKey);
  
  // Derive key with chaos diffusion
  const kdfKey = await chaosKDF(sharedSecret, envelope.ctx, envelope.intent);
  
  // Encrypt payload
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-gcm', kdfKey, iv);
  const encrypted = Buffer.concat([
    cipher.update(payload, 'utf8'),
    cipher.final()
  ]);
  const authTag = cipher.getAuthTag();
  
  // Return combined ciphertext
  return Buffer.concat([kemCipher, iv, authTag, encrypted]);
}

async function chaosKDF(sharedSecret, ctx, intent) {
  // Chaos-based key derivation
  const info = Buffer.concat([
    Buffer.from(scbe.sha256Object(ctx), 'hex'),
    Buffer.from(scbe.sha256Object(intent), 'hex')
  ]);
  
  return hkdf(sharedSecret, info, 32);
}
```

### 5.3 Signing (Orchestrator)

```javascript
async function signEnvelope(envelope) {
  // Load private key
  const privateKey = await kms.getKey('orchestrator-sig-private');
  
  // Serialize envelope (without sig field)
  const { sig, ...envelopeWithoutSig } = envelope;
  const message = Buffer.from(scbe.canonicalize(envelopeWithoutSig), 'utf8');
  
  // Sign with ML-DSA
  const signature = MLDsa65.sign(privateKey, message);
  
  return signature.toString('base64');
}
```

## Phase 6: Provider Integration (Week 6)

### 6.1 Provider Request Handler

```javascript
app.post('/provider/process', async (req, res) => {
  const envelope = req.body;
  
  try {
    // Verify orchestrator signature
    const isValid = await verifyOrchestratorSignature(envelope);
    if (!isValid) {
      return res.status(401).json({ error: 'Invalid signature' });
    }
    
    // Decrypt payload
    const payload = await decryptPayload(envelope.crypto.cipher_b64);
    
    // Process request
    const result = await processRequest(payload);
    
    // Encrypt response
    const responseCipher = await encryptPayload(JSON.stringify(result));
    
    // Create response envelope
    const responseEnvelope = {
      ...envelope,
      crypto: {
        ...envelope.crypto,
        cipher_b64: responseCipher.toString('base64')
      }
    };
    
    // Sign response
    const signature = await signResponse(responseEnvelope);
    const signedResponse = scbe.addProviderSignature(responseEnvelope, signature);
    
    res.json(signedResponse);
    
  } catch (error) {
    logger.error('Provider error:', error);
    res.status(500).json({ error: 'Processing failed' });
  }
});
```

## Testing

### Unit Tests

```javascript
const scbe = require('./scbe');

describe('SCBE Envelope', () => {
  it('should create valid envelope', () => {
    const envelope = scbe.buildEnvelope({
      ctx: { ts: 1000, device_id: 'test', threat_level: 1, entropy: 0.5, server_load: 0.5, stability: 0.9 },
      intent: { primary: 'test', modifier: 'test', harmonic: 3, phase_deg: 45 },
      trajectory: { epoch: 900, period_s: 3600, slot_id: 'test', waypoint: 1 },
      aad: { route_hint: 'test', run_id: 'test', step_no: 1 },
      crypto: { cipher_b64: 'dGVzdA==' }
    });
    
    expect(envelope.ver).toBe('scbe-2.0');
    expect(envelope.commit.ctx_sha256).toBeDefined();
  });
});
```

### Integration Tests

```bash
# Run security test suite
cd security/scbe
node tests/security-tests.js
```

### Load Testing

```javascript
// Test verification latency under load
async function loadTest() {
  const envelopes = Array(1000).fill(null).map(() => createTestEnvelope());
  
  const startTime = Date.now();
  await Promise.all(envelopes.map(e => scbe.runVerificationPipeline(e, config)));
  const duration = Date.now() - startTime;
  
  console.log(`Processed ${envelopes.length} envelopes in ${duration}ms`);
  console.log(`Throughput: ${(envelopes.length / duration * 1000).toFixed(0)} envelopes/sec`);
}
```

## Deployment Checklist

- [ ] Install SCBE module
- [ ] Implement deterministic context collection
- [ ] Configure intent policies
- [ ] Initialize trust store with providers
- [ ] Implement verification endpoint
- [ ] Add fail-to-noise error handling
- [ ] Configure metrics export
- [ ] Set up alerting thresholds
- [ ] Implement coherence tracking
- [ ] Schedule global trust decay
- [ ] Generate PQC keys
- [ ] Implement signing/verification
- [ ] Test security scenarios
- [ ] Load test verification pipeline
- [ ] Document provider integration
- [ ] Create runbook for operations

## Operations

### Monitoring

```bash
# Check swarm trust
curl http://orchestrator/metrics | grep swarm_trust_avg

# Check rejection rates
curl http://orchestrator/metrics | grep scbe_verify_reject_total

# Check phase skew
curl http://orchestrator/metrics | grep scbe_phase_skew_deg
```

### Troubleshooting

**High rejection rate:**
1. Check which gate is failing most
2. Review threshold configurations
3. Check for clock drift (phase skew p95)

**Low swarm trust:**
1. Identify providers with low trust
2. Review coherence scores
3. Check for sustained anomalies

**Phase misalignment:**
1. Verify NTP/GPS clock source
2. Check trajectory epoch configuration
3. Review period_s settings

## Support

- **Documentation:** `security/scbe/README.md`
- **Examples:** `security/scbe/examples/`
- **Tests:** `security/scbe/tests/`
- **Issues:** GitHub Issues

## Appendix: Key Management

### Production Key Storage

```javascript
// Use AWS KMS, Azure Key Vault, or HashiCorp Vault
const kms = require('@aws-sdk/client-kms');

async function storeKey(keyId, keyMaterial) {
  // Seal with KMS
  const result = await kms.encrypt({
    KeyId: 'alias/scbe-master-key',
    Plaintext: keyMaterial
  });
  
  // Store encrypted key
  await database.saveKey(keyId, result.CiphertextBlob);
}

async function getKey(keyId) {
  // Retrieve encrypted key
  const encrypted = await database.getKey(keyId);
  
  // Unseal with KMS
  const result = await kms.decrypt({
    CiphertextBlob: encrypted
  });
  
  return result.Plaintext;
}
```

### Key Rotation

```javascript
// Quarterly key rotation
schedule.scheduleJob('0 0 1 */3 *', async () => {
  logger.info('Starting key rotation...');
  
  // Generate new keys
  const newKemKeys = MLKem768.generateKeyPair();
  const newSigKeys = MLDsa65.generateKeyPair();
  
  // Store with versioning
  await kms.storeKey('orchestrator-kem-private-v2', newKemKeys.privateKey);
  await kms.storeKey('orchestrator-sig-private-v2', newSigKeys.privateKey);
  
  // Distribute new public keys
  await distributePubKey('orchestrator-kem-public-v2', newKemKeys.publicKey);
  await distributePubKey('orchestrator-sig-public-v2', newSigKeys.publicKey);
  
  // Update active version
  await config.setActiveKeyVersion(2);
  
  logger.info('Key rotation complete');
});
```
