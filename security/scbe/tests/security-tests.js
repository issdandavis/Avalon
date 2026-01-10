/**
 * SCBE Test Suite
 * Tests for the five critical security scenarios from the problem statement
 */

const { buildEnvelope } = require('../core/envelope-builder');
const { runVerificationPipeline } = require('../verification/pipeline');
const { TrustStore } = require('../verification/trust-store');

/**
 * Test 1: Replay Attack
 * Same payload with ts+300s should fail phase check
 */
async function testReplayAttack() {
  console.log('\n=== Test 1: Replay Attack ===');
  
  const baseTs = Math.floor(Date.now() / 1000);
  const epoch = baseTs - 1000;
  
  // Create original envelope
  const envelope = buildEnvelope({
    ctx: {
      ts: baseTs,
      device_id: 'device_123',
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
      epoch,
      period_s: 3600,
      slot_id: 'daily-08-12-16-20',
      waypoint: 1
    },
    aad: {
      route_hint: 'openai',
      run_id: 'run_123',
      step_no: 1
    },
    crypto: {
      cipher_b64: Buffer.from('original_encrypted_data').toString('base64')
    }
  });
  
  // First request should pass (assuming permissive config)
  const config1 = {
    currentTs: baseTs,
    energyConfig: { mean: 1.0, std: 0.5, k: 5.0, epsilon: 0.05 }
  };
  
  const result1 = await runVerificationPipeline(envelope, config1);
  console.log('Original request:', result1.success ? 'PASS' : 'FAIL', result1.reason);
  
  // Replay same envelope 300s later
  const replayTs = baseTs + 300;
  const config2 = {
    currentTs: replayTs,
    energyConfig: { mean: 1.0, std: 0.5, k: 5.0, epsilon: 0.05 }
  };
  
  const result2 = await runVerificationPipeline(envelope, config2);
  console.log('Replayed request (+300s):', result2.success ? 'PASS' : 'FAIL', result2.reason);
  
  if (!result2.success && result2.reason.includes('trajectory')) {
    console.log('✓ Replay attack correctly rejected');
    return true;
  } else {
    console.log('✗ Replay attack was not rejected');
    return false;
  }
}

/**
 * Test 2: Confused Deputy
 * Changing route_hint without changing intent_sha256 should fail
 */
async function testConfusedDeputy() {
  console.log('\n=== Test 2: Confused Deputy ===');
  
  const baseTs = Math.floor(Date.now() / 1000);
  const epoch = baseTs - 100;
  
  const envelope = buildEnvelope({
    ctx: {
      ts: baseTs,
      device_id: 'device_123',
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
      epoch,
      period_s: 3600,
      slot_id: 'daily-08-12-16-20',
      waypoint: 1
    },
    aad: {
      route_hint: 'openai',
      run_id: 'run_123',
      step_no: 1
    },
    crypto: {
      cipher_b64: Buffer.from('original_encrypted_data').toString('base64')
    }
  });
  
  // Now attacker changes route_hint without updating commit hash
  const tamperedEnvelope = {
    ...envelope,
    aad: {
      ...envelope.aad,
      route_hint: 'anthropic'  // Changed!
    }
    // commit.aad_sha256 is NOT updated - this is the attack
  };
  
  const config = {
    currentTs: baseTs,
    energyConfig: { mean: 1.0, std: 0.5, k: 5.0, epsilon: 0.05 }
  };
  
  const result = await runVerificationPipeline(tamperedEnvelope, config);
  console.log('Tampered request:', result.success ? 'PASS' : 'FAIL', result.reason);
  
  if (!result.success && result.reason.includes('commit')) {
    console.log('✓ Confused deputy attack correctly rejected');
    return true;
  } else {
    console.log('✗ Confused deputy attack was not rejected');
    return false;
  }
}

/**
 * Test 3: Low-grade Collusion
 * Two agents mirroring outputs should decay trust
 */
async function testLowGradeCollusion() {
  console.log('\n=== Test 3: Low-grade Collusion ===');
  
  const trustStore = new TrustStore();
  trustStore.initialize('agent_1', 0.8);
  trustStore.initialize('agent_2', 0.8);
  
  console.log('Initial trust - agent_1:', trustStore.getTrust('agent_1'));
  console.log('Initial trust - agent_2:', trustStore.getTrust('agent_2'));
  
  // Simulate 20 rounds where both agents show suspicious behavior
  // High coherence (mirroring) + deviation penalty
  for (let i = 0; i < 20; i++) {
    // Both agents get low validity scores due to collusion
    const validity = 0.1;  // Highly suspicious behavior (collusion detected)
    
    trustStore.updateTrust('agent_1', validity);
    trustStore.updateTrust('agent_2', validity);
  }
  
  const finalTrust1 = trustStore.getTrust('agent_1');
  const finalTrust2 = trustStore.getTrust('agent_2');
  
  console.log('Final trust - agent_1:', finalTrust1);
  console.log('Final trust - agent_2:', finalTrust2);
  
  const excluded1 = trustStore.shouldExclude('agent_1');
  const excluded2 = trustStore.shouldExclude('agent_2');
  
  console.log('agent_1 excluded:', excluded1);
  console.log('agent_2 excluded:', excluded2);
  
  if (excluded1 && excluded2) {
    console.log('✓ Colluding agents correctly excluded');
    return true;
  } else {
    console.log('✗ Colluding agents were not excluded');
    return false;
  }
}

/**
 * Test 4: Key Theft
 * Same envelope from new device_id should fail
 */
async function testKeyTheft() {
  console.log('\n=== Test 4: Key Theft ===');
  
  const baseTs = Math.floor(Date.now() / 1000);
  const epoch = baseTs - 100;
  
  const originalEnvelope = buildEnvelope({
    ctx: {
      ts: baseTs,
      device_id: 'device_123',
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
      epoch,
      period_s: 3600,
      slot_id: 'daily-08-12-16-20',
      waypoint: 1
    },
    aad: {
      route_hint: 'openai',
      run_id: 'run_123',
      step_no: 1
    },
    crypto: {
      cipher_b64: Buffer.from('original_encrypted_data').toString('base64')
    }
  });
  
  // Attacker tries to use stolen key from different device
  const stolenEnvelope = buildEnvelope({
    ctx: {
      ts: baseTs,
      device_id: 'stolen_device_999',  // Different device!
      threat_level: 5,  // Suspicious high threat
      entropy: 0.8,
      server_load: 0.7,
      stability: 0.6
    },
    intent: originalEnvelope.intent,
    trajectory: originalEnvelope.trajectory,
    aad: originalEnvelope.aad,
    crypto: {
      // Trying to reuse same ciphertext (key theft scenario)
      cipher_b64: originalEnvelope.crypto.cipher_b64
    }
  });
  
  const config = {
    currentTs: baseTs,
    energyConfig: { mean: 1.0, std: 0.5, k: 3.0, epsilon: 0.1 }
  };
  
  const result = await runVerificationPipeline(stolenEnvelope, config);
  console.log('Stolen key request:', result.success ? 'PASS' : 'FAIL', result.reason);
  
  // Should fail due to ctx_sha256 mismatch or neural energy
  if (!result.success) {
    console.log('✓ Key theft correctly rejected');
    return true;
  } else {
    console.log('✗ Key theft was not rejected');
    return false;
  }
}

/**
 * Test 5: Provider Compromise
 * Sustained coherence drift should exclude provider
 */
async function testProviderCompromise() {
  console.log('\n=== Test 5: Provider Compromise ===');
  
  const trustStore = new TrustStore();
  trustStore.initialize('provider_compromised', 0.9);
  
  console.log('Initial trust:', trustStore.getTrust('provider_compromised'));
  
  // Simulate 20 calls with low coherence (compromised behavior)
  for (let i = 0; i < 20; i++) {
    const validity = 0.2;  // Low coherence = compromised
    trustStore.updateTrust('provider_compromised', validity);
  }
  
  const finalTrust = trustStore.getTrust('provider_compromised');
  const excluded = trustStore.shouldExclude('provider_compromised');
  
  console.log('Final trust:', finalTrust);
  console.log('Provider excluded:', excluded);
  
  if (excluded) {
    console.log('✓ Compromised provider correctly excluded');
    return true;
  } else {
    console.log('✗ Compromised provider was not excluded');
    return false;
  }
}

/**
 * Run all tests
 */
async function runAllTests() {
  console.log('======================================');
  console.log('SCBE Security Test Suite');
  console.log('======================================');
  
  const results = {
    replay: await testReplayAttack(),
    confusedDeputy: await testConfusedDeputy(),
    collusion: await testLowGradeCollusion(),
    keyTheft: await testKeyTheft(),
    providerCompromise: await testProviderCompromise()
  };
  
  console.log('\n======================================');
  console.log('Test Results Summary');
  console.log('======================================');
  console.log('Replay Attack:', results.replay ? '✓ PASS' : '✗ FAIL');
  console.log('Confused Deputy:', results.confusedDeputy ? '✓ PASS' : '✗ FAIL');
  console.log('Low-grade Collusion:', results.collusion ? '✓ PASS' : '✗ FAIL');
  console.log('Key Theft:', results.keyTheft ? '✓ PASS' : '✗ FAIL');
  console.log('Provider Compromise:', results.providerCompromise ? '✓ PASS' : '✗ FAIL');
  
  const allPassed = Object.values(results).every(r => r);
  console.log('\nOverall:', allPassed ? '✓ ALL TESTS PASSED' : '✗ SOME TESTS FAILED');
  
  return allPassed;
}

// Run tests if executed directly
if (require.main === module) {
  runAllTests().then(success => {
    process.exit(success ? 0 : 1);
  }).catch(error => {
    console.error('Test suite error:', error);
    process.exit(1);
  });
}

module.exports = {
  testReplayAttack,
  testConfusedDeputy,
  testLowGradeCollusion,
  testKeyTheft,
  testProviderCompromise,
  runAllTests
};
