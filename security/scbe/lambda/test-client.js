#!/usr/bin/env node

/**
 * SCBE v2.0 Test Client
 * Demonstrates manifold-gated dual-lane key schedule
 */

const https = require('https');
const http = require('http');

// Configuration
const config = {
  // Set to your Lambda API endpoint after deployment
  apiEndpoint: process.env.SCBE_API_ENDPOINT || 'http://localhost:3000',
  verbose: true
};

/**
 * Make HTTP request
 */
function request(method, path, body = null) {
  return new Promise((resolve, reject) => {
    const url = new URL(config.apiEndpoint + path);
    const isHttps = url.protocol === 'https:';
    const lib = isHttps ? https : http;

    const options = {
      hostname: url.hostname,
      port: url.port || (isHttps ? 443 : 80),
      path: url.pathname + url.search,
      method: method,
      headers: {
        'Content-Type': 'application/json'
      }
    };

    if (body) {
      const bodyStr = JSON.stringify(body);
      options.headers['Content-Length'] = Buffer.byteLength(bodyStr);
    }

    const req = lib.request(options, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          resolve({
            status: res.statusCode,
            data: JSON.parse(data)
          });
        } catch (error) {
          resolve({
            status: res.statusCode,
            data: data
          });
        }
      });
    });

    req.on('error', reject);

    if (body) {
      req.write(JSON.stringify(body));
    }

    req.end();
  });
}

/**
 * Test brain lane (fast, autonomous)
 */
async function testBrainLane() {
  console.log('\n=== Testing Brain Lane (Manifold-Gated Internal) ===');
  
  const payload = {
    operation: 'analyze',
    data: {
      input: 'Sample data for brain lane processing',
      priority: 'high'
    }
  };

  const context = {
    device_id: 'brain-test-device-001',
    run_id: `brain-run-${Date.now()}`,
    step_no: 1,
    phase_hint: 45
  };

  const response = await request('POST', '/api/brain-lane', { payload, context });
  
  if (config.verbose) {
    console.log('Status:', response.status);
    console.log('Response:', JSON.stringify(response.data, null, 2));
  }

  if (response.status === 200 && response.data.success) {
    console.log('✓ Brain lane: PASS');
    console.log(`  - Verification: ${response.data.verification_ms}ms`);
    console.log(`  - Trust score: ${response.data.trust_score}`);
    console.log(`  - Gates passed: ${response.data.gates_passed}`);
    return true;
  } else {
    console.log('✗ Brain lane: FAIL');
    console.log(`  - Reason: ${response.data.reason || 'Unknown'}`);
    return false;
  }
}

/**
 * Test oversight lane (strict, validated)
 */
async function testOversightLane() {
  console.log('\n=== Testing Oversight Lane (Manifold-Gated External) ===');
  
  const payload = {
    operation: 'validate',
    data: {
      input: 'Sample data for oversight lane processing',
      priority: 'standard'
    }
  };

  const context = {
    device_id: 'oversight-test-device-001',
    run_id: `oversight-run-${Date.now()}`,
    step_no: 1,
    waypoint: 0,
    phase_hint: 90
  };

  const response = await request('POST', '/api/oversight-lane', { payload, context });
  
  if (config.verbose) {
    console.log('Status:', response.status);
    console.log('Response:', JSON.stringify(response.data, null, 2));
  }

  if (response.status === 200 && response.data.success) {
    console.log('✓ Oversight lane: PASS');
    console.log(`  - Verification: ${response.data.verification_ms}ms`);
    console.log(`  - Trust score: ${response.data.trust_score}`);
    console.log(`  - Gates passed: ${response.data.gates_passed}`);
    console.log(`  - Drift amplified: ${response.data.drift_amplified.amplified ? 'YES' : 'NO'}`);
    console.log(`  - Coherence: ${response.data.drift_amplified.coherence.toFixed(3)}`);
    return true;
  } else {
    console.log('✗ Oversight lane: FAIL');
    console.log(`  - Reason: ${response.data.reason || 'Unknown'}`);
    return false;
  }
}

/**
 * Test lane comparison (demonstrates dual-lane key schedule)
 */
async function testLaneComparison() {
  console.log('\n=== Testing Dual-Lane Key Schedule ===');
  
  const testPayload = {
    operation: 'process',
    data: { value: 42, timestamp: Date.now() }
  };

  // Send same payload to both lanes
  const brainContext = {
    device_id: 'comparison-brain-001',
    run_id: `comparison-${Date.now()}`,
    step_no: 1
  };

  const oversightContext = {
    device_id: 'comparison-oversight-001',
    run_id: `comparison-${Date.now()}`,
    step_no: 1,
    waypoint: 0
  };

  const [brainRes, oversightRes] = await Promise.all([
    request('POST', '/api/brain-lane', { payload: testPayload, context: brainContext }),
    request('POST', '/api/oversight-lane', { payload: testPayload, context: oversightContext })
  ]);

  console.log('\nComparison Results:');
  console.log('─────────────────────────────────────────────');
  console.log('                    Brain Lane    Oversight Lane');
  console.log('─────────────────────────────────────────────');
  console.log(`Success:            ${brainRes.data.success ? '✓' : '✗'}            ${oversightRes.data.success ? '✓' : '✗'}`);
  
  if (brainRes.data.success && oversightRes.data.success) {
    console.log(`Verification (ms):  ${brainRes.data.verification_ms}           ${oversightRes.data.verification_ms}`);
    console.log(`Trust Score:        ${brainRes.data.trust_score}         ${oversightRes.data.trust_score}`);
    console.log(`Gates Passed:       ${brainRes.data.gates_passed}              ${oversightRes.data.gates_passed}`);
  }
  console.log('─────────────────────────────────────────────');
  
  console.log('\n✓ Dual-lane demonstration complete');
  console.log('  - Brain lane: Fast, autonomous (low oversight)');
  console.log('  - Oversight lane: Validated, coherence-tracked (high oversight)');
}

/**
 * Test trajectory + drift-amplified coherence
 */
async function testTrajectoryCoherence() {
  console.log('\n=== Testing Trajectory + Drift-Amplified Coherence ===');
  
  // Build a test envelope manually
  const scbe = require('../index');
  
  const envelope = scbe.buildEnvelope({
    ctx: {
      ts: Math.floor(Date.now() / 1000),
      device_id: 'coherence-test-001',
      threat_level: 3,
      entropy: 0.5,
      server_load: 0.4,
      stability: 0.85
    },
    intent: {
      primary: 'sil\'kor',
      modifier: 'nav\'een',
      harmonic: 3,
      phase_deg: 45
    },
    trajectory: {
      epoch: Math.floor(Date.now() / 1000) - 600,
      period_s: 3600,
      slot_id: 'coherence-test-slot',
      waypoint: 0
    },
    aad: {
      route_hint: 'test-provider',
      run_id: `coherence-${Date.now()}`,
      step_no: 1
    },
    crypto: {
      cipher_b64: Buffer.from(JSON.stringify({ test: 'data' })).toString('base64')
    }
  });

  const response = await request('POST', '/api/verify', { envelope });
  
  if (config.verbose) {
    console.log('Status:', response.status);
    console.log('Response:', JSON.stringify(response.data, null, 2));
  }

  if (response.status === 200 && response.data.success) {
    console.log('✓ Trajectory + coherence: PASS');
    console.log(`  - Verification: ${response.data.verification_ms}ms`);
    console.log(`  - Trajectory valid: ${response.data.trajectory_valid ? 'YES' : 'NO'}`);
    console.log(`  - Coherence authorized: ${response.data.coherence_authorized ? 'YES' : 'NO'}`);
    
    const drift = response.data.drift_amplification;
    console.log(`  - Phase skew: ${drift.phase_skew_deg.toFixed(2)}°`);
    console.log(`  - Energy margin: ${drift.energy_margin.toFixed(3)}`);
    console.log(`  - Coherence score: ${drift.coherence.toFixed(3)}`);
    console.log(`  - Amplified: ${drift.amplified ? 'YES' : 'NO'}`);
    return true;
  } else {
    console.log('✗ Trajectory + coherence: FAIL');
    console.log(`  - Reason: ${response.data.reason || 'Unknown'}`);
    return false;
  }
}

/**
 * Get metrics
 */
async function getMetrics() {
  console.log('\n=== Current Metrics ===');
  
  const response = await request('GET', '/api/metrics');
  
  if (response.status === 200) {
    const data = response.data;
    console.log('Trust Scores:');
    console.log(`  - Brain lane: ${data.trust_scores['brain-lane']}`);
    console.log(`  - Oversight lane: ${data.trust_scores['oversight-lane']}`);
    console.log(`  - Swarm entropy: ${data.swarm_entropy}`);
    
    if (data.alerts && data.alerts.length > 0) {
      console.log('\nAlerts:');
      data.alerts.forEach(alert => {
        console.log(`  - [${alert.severity}] ${alert.message}`);
      });
    } else {
      console.log('\n✓ No alerts');
    }
  }
}

/**
 * Check health
 */
async function checkHealth() {
  console.log('\n=== Health Check ===');
  
  const response = await request('GET', '/api/health');
  
  if (response.status === 200) {
    const data = response.data;
    console.log(`Status: ${data.status}`);
    console.log(`Version: ${data.version}`);
    console.log(`Brain lane: ${data.lanes.brain ? '✓ healthy' : '✗ unhealthy'}`);
    console.log(`Oversight lane: ${data.lanes.oversight ? '✓ healthy' : '✗ unhealthy'}`);
    return data.status === 'healthy';
  } else {
    console.log('✗ Health check failed');
    return false;
  }
}

/**
 * Run all tests
 */
async function runAllTests() {
  console.log('╔═══════════════════════════════════════════════════════════════╗');
  console.log('║                                                               ║');
  console.log('║          SCBE v2.0 - Dual-Lane Key Schedule Demo             ║');
  console.log('║                                                               ║');
  console.log('╚═══════════════════════════════════════════════════════════════╝');
  console.log(`\nAPI Endpoint: ${config.apiEndpoint}`);

  try {
    // Health check
    const healthy = await checkHealth();
    if (!healthy) {
      console.log('\n✗ System unhealthy, aborting tests');
      process.exit(1);
    }

    // Run tests
    const brainPass = await testBrainLane();
    const oversightPass = await testOversightLane();
    await testLaneComparison();
    const coherencePass = await testTrajectoryCoherence();
    
    // Get final metrics
    await getMetrics();

    // Summary
    console.log('\n╔═══════════════════════════════════════════════════════════════╗');
    console.log('║                       Test Summary                            ║');
    console.log('╚═══════════════════════════════════════════════════════════════╝');
    console.log(`Brain Lane:              ${brainPass ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`Oversight Lane:          ${oversightPass ? '✓ PASS' : '✗ FAIL'}`);
    console.log(`Trajectory + Coherence:  ${coherencePass ? '✓ PASS' : '✗ FAIL'}`);
    
    const allPass = brainPass && oversightPass && coherencePass;
    console.log(`\nOverall: ${allPass ? '✓ ALL TESTS PASSED' : '✗ SOME TESTS FAILED'}`);
    
    process.exit(allPass ? 0 : 1);
  } catch (error) {
    console.error('\n✗ Test error:', error.message);
    process.exit(1);
  }
}

// Run tests
if (require.main === module) {
  runAllTests();
}

module.exports = {
  testBrainLane,
  testOversightLane,
  testLaneComparison,
  testTrajectoryCoherence,
  getMetrics,
  checkHealth
};
