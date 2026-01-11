/**
 * AWS Lambda Handler for SCBE v2.0 System
 * Exposes API endpoints for testing manifold-gated dual-lane key schedule
 */

const scbe = require('../index');

// Global trust store (in production, use DynamoDB or similar)
const trustStore = new scbe.TrustStore();
trustStore.initialize('brain-lane', 0.9);
trustStore.initialize('oversight-lane', 0.85);
trustStore.initialize('openai', 0.8);
trustStore.initialize('anthropic', 0.8);

/**
 * Main Lambda handler
 */
exports.handler = async (event) => {
  console.log('Event:', JSON.stringify(event, null, 2));

  try {
    const path = event.path || event.rawPath || '/';
    const method = event.httpMethod || event.requestContext?.http?.method || 'GET';
    const body = event.body ? JSON.parse(event.body) : {};

    // Route to appropriate handler
    if (method === 'POST' && path === '/api/brain-lane') {
      return await handleBrainLane(body);
    } else if (method === 'POST' && path === '/api/oversight-lane') {
      return await handleOversightLane(body);
    } else if (method === 'POST' && path === '/api/verify') {
      return await handleVerify(body);
    } else if (method === 'GET' && path === '/api/metrics') {
      return handleMetrics();
    } else if (method === 'GET' && path === '/api/health') {
      return handleHealth();
    } else if (method === 'GET' && path === '/') {
      return handleRoot();
    } else {
      return createResponse(404, { error: 'Not found' });
    }
  } catch (error) {
    console.error('Error:', error);
    return createResponse(500, { error: error.message });
  }
};

/**
 * Brain Lane: Inside manifold-gated processing
 * Low oversight, high autonomy, optimized for speed
 */
async function handleBrainLane(body) {
  const { payload, context } = body;

  if (!payload || !context) {
    return createResponse(400, { error: 'Missing payload or context' });
  }

  // Build envelope for brain lane with permissive thresholds
  const envelope = scbe.buildEnvelope({
    ctx: {
      ts: Math.floor(Date.now() / 1000),
      device_id: context.device_id || 'brain-lane-default',
      threat_level: 1, // Low threat (internal processing)
      entropy: 0.3, // Low entropy (stable internal state)
      server_load: 0.2,
      stability: 0.95 // High stability
    },
    intent: {
      primary: 'sil\'kor', // Primary operation
      modifier: 'nav\'een', // Fast modifier
      harmonic: 2, // Low harmonic (fast lane)
      phase_deg: calculatePhaseForLane('brain', context)
    },
    trajectory: {
      epoch: Math.floor(Date.now() / 1000) - 300, // 5 min window
      period_s: 600, // 10 min period (short for brain lane)
      slot_id: 'brain-lane-fast',
      waypoint: 0
    },
    aad: {
      route_hint: 'brain-lane',
      run_id: context.run_id || `brain-${Date.now()}`,
      step_no: context.step_no || 0
    },
    crypto: {
      cipher_b64: Buffer.from(JSON.stringify(payload)).toString('base64')
    }
  });

  // Verify with permissive config (brain lane needs speed)
  const config = {
    currentTs: Math.floor(Date.now() / 1000),
    energyConfig: {
      mean: 0.5,
      std: 0.4,
      k: 5.0, // Very permissive
      epsilon: 0.05
    },
    trustStore
  };

  const startTime = Date.now();
  const result = await scbe.runVerificationPipeline(envelope, config);
  const duration = Date.now() - startTime;

  scbe.recordVerificationLatency(duration);

  if (result.success) {
    // Update trust (brain lane gets rewarded for fast processing)
    const validity = scbe.computeValidity({
      neuralPassed: true,
      coherence: 0.95,
      deviationPenalty: 0.02
    });
    trustStore.updateTrust('brain-lane', validity);
    scbe.updateSwarmMetrics(trustStore);

    return createResponse(200, {
      success: true,
      lane: 'brain',
      envelope_id: envelope.commit.ctx_sha256.substring(0, 16),
      verification_ms: duration,
      gates_passed: result.results.gates.length,
      trust_score: trustStore.getTrust('brain-lane').toFixed(3),
      message: 'Brain lane processed: fast autonomous execution'
    });
  } else {
    scbe.recordRejection(result.reason);
    return createResponse(403, {
      success: false,
      lane: 'brain',
      reason: result.reason,
      verification_ms: duration,
      noise_envelope: result.noiseEnvelope
    });
  }
}

/**
 * Oversight Lane: External manifold-gated processing
 * High oversight, lower autonomy, stricter validation
 */
async function handleOversightLane(body) {
  const { payload, context } = body;

  if (!payload || !context) {
    return createResponse(400, { error: 'Missing payload or context' });
  }

  // Build envelope for oversight lane with strict thresholds
  const envelope = scbe.buildEnvelope({
    ctx: {
      ts: Math.floor(Date.now() / 1000),
      device_id: context.device_id || 'oversight-lane-default',
      threat_level: 5, // Moderate threat (external processing)
      entropy: 0.7, // Higher entropy (external variability)
      server_load: 0.5,
      stability: 0.75 // Lower stability tolerance
    },
    intent: {
      primary: 'sil\'kor',
      modifier: 'keth\'ara', // Careful modifier
      harmonic: 5, // Higher harmonic (oversight lane)
      phase_deg: calculatePhaseForLane('oversight', context)
    },
    trajectory: {
      epoch: Math.floor(Date.now() / 1000) - 1800, // 30 min window
      period_s: 3600, // 1 hour period (longer for oversight)
      slot_id: 'oversight-lane-strict',
      waypoint: context.waypoint || 0
    },
    aad: {
      route_hint: 'oversight-lane',
      run_id: context.run_id || `oversight-${Date.now()}`,
      step_no: context.step_no || 0
    },
    crypto: {
      cipher_b64: Buffer.from(JSON.stringify(payload)).toString('base64')
    }
  });

  // Verify with strict config (oversight lane needs validation)
  const config = {
    currentTs: Math.floor(Date.now() / 1000),
    energyConfig: {
      mean: 1.0,
      std: 0.3,
      k: 2.5, // Strict threshold
      epsilon: 0.15
    },
    intentPolicy: {
      providers: {
        'oversight-lane': {
          allowed_intents: [
            'sil\'kor:keth\'ara',
            'terra\'bind:keth\'ara'
          ]
        }
      }
    },
    trustStore
  };

  const startTime = Date.now();
  const result = await scbe.runVerificationPipeline(envelope, config);
  const duration = Date.now() - startTime;

  scbe.recordVerificationLatency(duration);

  if (result.success) {
    // Update trust with coherence tracking
    const validity = scbe.computeValidity({
      neuralPassed: true,
      coherence: 0.85,
      deviationPenalty: 0.1
    });
    trustStore.updateTrust('oversight-lane', validity);
    scbe.updateSwarmMetrics(trustStore);

    return createResponse(200, {
      success: true,
      lane: 'oversight',
      envelope_id: envelope.commit.ctx_sha256.substring(0, 16),
      verification_ms: duration,
      gates_passed: result.results.gates.length,
      trust_score: trustStore.getTrust('oversight-lane').toFixed(3),
      drift_amplified: calculateDriftAmplification(result),
      message: 'Oversight lane processed: validated with drift amplification'
    });
  } else {
    scbe.recordRejection(result.reason);
    return createResponse(403, {
      success: false,
      lane: 'oversight',
      reason: result.reason,
      verification_ms: duration,
      noise_envelope: result.noiseEnvelope
    });
  }
}

/**
 * Generic verify endpoint (demonstrates trajectory + drift-amplified coherence)
 */
async function handleVerify(body) {
  const { envelope } = body;

  if (!envelope) {
    return createResponse(400, { error: 'Missing envelope' });
  }

  try {
    // Validate envelope structure
    scbe.validateEnvelope(envelope);

    // Verify commit hashes
    if (!scbe.verifyCommitHashes(envelope)) {
      return createResponse(400, { error: 'Commit hash mismatch' });
    }

    // Full verification with both trajectory and coherence checks
    const config = {
      currentTs: Math.floor(Date.now() / 1000),
      energyConfig: {
        mean: 1.0,
        std: 0.3,
        k: 3.0,
        epsilon: 0.1
      },
      trustStore
    };

    const startTime = Date.now();
    const result = await scbe.runVerificationPipeline(envelope, config);
    const duration = Date.now() - startTime;

    scbe.recordVerificationLatency(duration);

    if (result.success) {
      // Calculate drift amplification score
      const driftScore = calculateDriftAmplification(result);
      
      return createResponse(200, {
        success: true,
        verification_ms: duration,
        gates: result.results.gates.map(g => ({
          gate: g.gate,
          passed: g.passed,
          metadata: g.metadata
        })),
        trajectory_valid: true,
        drift_amplification: driftScore,
        coherence_authorized: driftScore.coherence > 0.7
      });
    } else {
      scbe.recordRejection(result.reason);
      return createResponse(403, {
        success: false,
        reason: result.reason,
        verification_ms: duration,
        noise_returned: true
      });
    }
  } catch (error) {
    return createResponse(400, { error: error.message });
  }
}

/**
 * Metrics endpoint
 */
function handleMetrics() {
  const summary = scbe.getMetricsSummary();
  const alerts = scbe.checkAlerts({
    swarm_trust_avg: 0.5,
    gft_score: 0.8,
    phase_skew_p95: 30
  });

  return createResponse(200, {
    summary,
    alerts,
    trust_scores: {
      'brain-lane': trustStore.getTrust('brain-lane').toFixed(3),
      'oversight-lane': trustStore.getTrust('oversight-lane').toFixed(3),
      'openai': trustStore.getTrust('openai').toFixed(3),
      'anthropic': trustStore.getTrust('anthropic').toFixed(3)
    },
    swarm_entropy: trustStore.getSwarmEntropy().toFixed(3)
  });
}

/**
 * Health check endpoint
 */
function handleHealth() {
  return createResponse(200, {
    status: 'healthy',
    version: scbe.SCBE_VERSION,
    timestamp: Math.floor(Date.now() / 1000),
    lanes: {
      brain: trustStore.getTrust('brain-lane') > 0.3,
      oversight: trustStore.getTrust('oversight-lane') > 0.3
    }
  });
}

/**
 * Root endpoint - API documentation
 */
function handleRoot() {
  return createResponse(200, {
    name: 'SCBE v2.0 Lambda API',
    version: scbe.SCBE_VERSION,
    endpoints: {
      'POST /api/brain-lane': 'Manifold-gated brain lane (fast, autonomous)',
      'POST /api/oversight-lane': 'Manifold-gated oversight lane (strict, validated)',
      'POST /api/verify': 'Generic verification (trajectory + drift coherence)',
      'GET /api/metrics': 'Get metrics and trust scores',
      'GET /api/health': 'Health check'
    },
    patent_seams: {
      manifold_gated_dual_lane: 'brain-lane vs oversight-lane endpoints',
      trajectory_drift_coherence: '/api/verify endpoint'
    }
  });
}

/**
 * Calculate phase for lane type
 */
function calculatePhaseForLane(lane, context) {
  const basePhase = context.phase_hint || 45;
  
  if (lane === 'brain') {
    // Brain lane: optimized for speed, lower phase variance
    return (basePhase + Math.floor(Date.now() / 10000) % 60) % 360;
  } else {
    // Oversight lane: stricter phase alignment
    return (basePhase + Math.floor(Date.now() / 30000) % 90) % 360;
  }
}

/**
 * Calculate drift amplification score
 */
function calculateDriftAmplification(verificationResult) {
  const gates = verificationResult.results.gates;
  
  // Extract phase skew if available
  const trajectoryGate = gates.find(g => g.gate === 'trajectory');
  const phaseSkew = trajectoryGate?.metadata?.phase_skew || 0;
  
  // Calculate coherence from gate metadata
  const neuralGate = gates.find(g => g.gate === 'neural');
  const energyMargin = neuralGate?.metadata?.margin || 0.5;
  
  // Drift amplification: lower phase skew + higher margin = better coherence
  const coherence = Math.max(0, Math.min(1, (1 - phaseSkew / 180) * energyMargin));
  
  return {
    phase_skew_deg: phaseSkew,
    energy_margin: energyMargin,
    coherence: coherence,
    amplified: coherence > 0.7
  };
}

/**
 * Create HTTP response
 */
function createResponse(statusCode, body) {
  return {
    statusCode,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET,POST,OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type'
    },
    body: JSON.stringify(body, null, 2)
  };
}
