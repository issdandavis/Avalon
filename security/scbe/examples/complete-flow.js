/**
 * SCBE Example: Gateway Implementation
 * Shows how to create envelopes at the gateway layer
 */

const scbe = require('../index');

/**
 * Gateway: Create and send envelope
 */
async function gatewayExample() {
  console.log('=== Gateway Example ===\n');

  // 1. Gather context (deterministic, no random values)
  const ctx = {
    ts: Math.floor(Date.now() / 1000),  // Seconds, not milliseconds
    device_id: 'user_device_5a2k9',
    threat_level: 2,
    entropy: 0.72,  // Derived from request, NOT random
    server_load: 0.45,  // Current load metric
    stability: 0.89  // System stability metric
  };

  // 2. Define intent
  const intent = {
    primary: 'sil\'kor',  // Primary operation
    modifier: 'nav\'een',  // Modifier
    harmonic: 3,  // 1-7
    phase_deg: 45  // 0-359
  };

  // 3. Define trajectory
  const trajectory = {
    epoch: Math.floor(Date.now() / 1000) - 1000,  // Policy window start
    period_s: 3600,  // 1 hour period
    slot_id: 'daily-08-12-16-20',  // Schedule ID
    waypoint: 1  // Step in schedule
  };

  // 4. Define AAD (Additional Authenticated Data)
  const aad = {
    route_hint: 'openai',  // Target provider
    run_id: 'run_xyz123',
    step_no: 7
  };

  // 5. Encrypt payload (simplified - use real encryption in production)
  const sensitivePayload = JSON.stringify({
    prompt: 'Analyze this data...',
    context: { user_id: 'user123' }
  });
  const cipher_b64 = Buffer.from(sensitivePayload).toString('base64');

  // 6. Build envelope
  const envelope = scbe.buildEnvelope({
    ctx,
    intent,
    trajectory,
    aad,
    crypto: {
      cipher_b64,
      // salt_q_b64 will be auto-generated if not provided
      h: {
        d: 4,
        R: 1.5,
        H: Math.pow(1.5, 16),
        n_iter: 6500
      }
    }
  });

  console.log('Envelope created:');
  console.log('- Version:', envelope.ver);
  console.log('- Context hash:', envelope.commit.ctx_sha256.substring(0, 16) + '...');
  console.log('- Intent hash:', envelope.commit.intent_sha256.substring(0, 16) + '...');
  console.log('- Provider:', envelope.aad.route_hint);

  // 7. Sign envelope (in production, use real ML-DSA signature)
  const orchestratorSig = Buffer.from('mock_signature').toString('base64');
  const signedEnvelope = scbe.addOrchestratorSignature(envelope, orchestratorSig);

  console.log('\nEnvelope signed and ready to send to orchestrator');
  
  return signedEnvelope;
}

/**
 * Orchestrator: Verify and process envelope
 */
async function orchestratorExample(envelope) {
  console.log('\n=== Orchestrator Example ===\n');

  // 1. Initialize trust store
  const trustStore = new scbe.TrustStore();
  trustStore.initialize('openai', 0.8);
  trustStore.initialize('anthropic', 0.7);

  // 2. Configure verification
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
      epsilon: 0.1
    },
    
    trustStore
  };

  // 3. Run verification pipeline
  console.log('Running verification pipeline...');
  const startTime = Date.now();
  const result = await scbe.runVerificationPipeline(envelope, config);
  const duration = Date.now() - startTime;

  // 4. Record metrics
  scbe.recordVerificationLatency(duration);

  if (result.success) {
    console.log('✓ Verification PASSED');
    console.log('Gates passed:', result.results.gates.length);
    
    // 5. Process envelope (decrypt, route to provider, etc.)
    console.log('\nProcessing envelope...');
    console.log('- Routing to:', envelope.aad.route_hint);
    
    // 6. Update trust on success
    const validity = scbe.computeValidity({
      neuralPassed: true,
      coherence: 0.95,
      deviationPenalty: 0.05
    });
    trustStore.updateTrust(envelope.aad.route_hint, validity);
    
    // 7. Record success
    scbe.recordEnvelopeProcessed(true);
    scbe.updateSwarmMetrics(trustStore);
    
    return { success: true, envelope };
    
  } else {
    console.log('✗ Verification FAILED');
    console.log('Reason:', result.reason);
    console.log('Failed at gate:', result.results.gates[result.results.gates.length - 1].gate);
    
    // 8. Record rejection
    scbe.recordRejection(result.reason);
    scbe.recordEnvelopeProcessed(false);
    
    // 9. Return noise envelope (same shape, no information leakage)
    console.log('\nReturning noise response (fail-to-noise)');
    return { success: false, envelope: result.noiseEnvelope };
  }
}

/**
 * Provider: Process and return signed response
 */
async function providerExample(envelope) {
  console.log('\n=== Provider Example ===\n');

  // 1. Verify orchestrator signature (simplified)
  console.log('Verifying orchestrator signature...');
  if (!envelope.sig.orchestrator_sig_b64) {
    throw new Error('Missing orchestrator signature');
  }
  console.log('✓ Orchestrator signature valid');

  // 2. Process request (decrypt, execute, encrypt response)
  console.log('\nProcessing request...');
  const responsePayload = JSON.stringify({
    result: 'Analysis complete',
    data: { score: 0.92 }
  });
  const responseCipher = Buffer.from(responsePayload).toString('base64');

  // 3. Create response envelope
  const responseEnvelope = {
    ...envelope,
    crypto: {
      ...envelope.crypto,
      cipher_b64: responseCipher
    }
  };

  // 4. Sign response
  const providerSig = Buffer.from('provider_signature').toString('base64');
  const signedResponse = scbe.addProviderSignature(responseEnvelope, providerSig);

  console.log('✓ Response signed');
  console.log('Returning to orchestrator');

  return signedResponse;
}

/**
 * Run complete flow
 */
async function runCompleteFlow() {
  console.log('======================================');
  console.log('SCBE Complete Flow Example');
  console.log('======================================\n');

  try {
    // Step 1: Gateway creates envelope
    const envelope = await gatewayExample();

    // Step 2: Orchestrator verifies
    const verifyResult = await orchestratorExample(envelope);

    if (verifyResult.success) {
      // Step 3: Provider processes
      const response = await providerExample(verifyResult.envelope);

      // Step 4: Orchestrator verifies provider response
      console.log('\n=== Orchestrator: Verify Provider Response ===\n');
      if (response.sig.provider_sig_b64) {
        console.log('✓ Provider signature valid');
        console.log('✓ Request-response binding verified');
      }

      console.log('\n✓ Complete flow successful');
    } else {
      console.log('\n✗ Flow terminated at verification (noise returned)');
    }

    // Step 5: Show metrics
    console.log('\n=== Metrics Summary ===\n');
    const summary = scbe.getMetricsSummary();
    console.log('Swarm trust average:', summary.swarm_trust_avg.toFixed(3));
    console.log('Phase skew p95:', summary.phase_skew_p95 || 'N/A');
    console.log('Envelopes processed:', 
      (summary.rejections.fractal || 0) + 1);

  } catch (error) {
    console.error('Error in flow:', error.message);
    throw error;
  }
}

// Run example
if (require.main === module) {
  runCompleteFlow().catch(error => {
    console.error('Fatal error:', error);
    process.exit(1);
  });
}

module.exports = {
  gatewayExample,
  orchestratorExample,
  providerExample,
  runCompleteFlow
};
