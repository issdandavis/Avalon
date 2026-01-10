/**
 * SCBE Verification Pipeline
 * Implements the ordered verification gates: schema → fractal → intent → trajectory → neural → swarm → crypto
 */

const { validateEnvelope } = require('../core/envelope-schema');
const { verifyCommitHashes, generateDeterministicNoise, computeDeterministicDelay } = require('../core/crypto-utils');
const { calculateCurrentPhase, isPhaseWithinTolerance, createNoiseResponse } = require('../core/envelope-builder');

/**
 * Verification result structure
 */
class VerificationResult {
  constructor(passed, reason = null, metadata = {}) {
    this.passed = passed;
    this.reason = reason;
    this.metadata = metadata;
  }

  static pass(metadata = {}) {
    return new VerificationResult(true, null, metadata);
  }

  static fail(reason, metadata = {}) {
    return new VerificationResult(false, reason, metadata);
  }
}

/**
 * Gate 1: Schema validation and clamping
 * Validates envelope structure and ensures commit hashes match
 */
function gate1_schemaValidation(envelope) {
  try {
    // Validate envelope structure
    const validated = validateEnvelope(envelope);

    // Verify commit hashes
    if (!verifyCommitHashes(validated)) {
      return VerificationResult.fail('schema_commit_mismatch', {
        step: 'schema'
      });
    }

    return VerificationResult.pass({ validated });
  } catch (error) {
    return VerificationResult.fail('schema_invalid', {
      step: 'schema',
      error: error.message
    });
  }
}

/**
 * Gate 2: Fractal gate (chaos-based rejection)
 * Computes Julia set iteration count for context-derived z0 and intent-derived c
 */
function gate2_fractalGate(envelope) {
  const { ctx, intent, crypto } = envelope;
  
  // Derive z0 from context (using normalized values)
  const z0_real = ctx.entropy * 2 - 1;  // Map [0,1] to [-1,1]
  const z0_imag = ctx.server_load * 2 - 1;
  
  // Derive c from intent (using harmonic and phase)
  const phase_rad = (intent.phase_deg * Math.PI) / 180;
  const c_real = Math.cos(phase_rad) * (intent.harmonic / 7);
  const c_imag = Math.sin(phase_rad) * (intent.harmonic / 7);
  
  // Julia set iteration
  let z_real = z0_real;
  let z_imag = z0_imag;
  let iterations = 0;
  const maxIter = crypto.h.n_iter;
  const escapeRadius = crypto.h.R;
  const escapeRadiusSq = escapeRadius * escapeRadius;
  
  while (iterations < maxIter) {
    const z_real_sq = z_real * z_real;
    const z_imag_sq = z_imag * z_imag;
    
    if (z_real_sq + z_imag_sq > escapeRadiusSq) {
      break;
    }
    
    const new_z_real = z_real_sq - z_imag_sq + c_real;
    const new_z_imag = 2 * z_real * z_imag + c_imag;
    
    z_real = new_z_real;
    z_imag = new_z_imag;
    iterations++;
  }
  
  // Pass if we reached max iterations (point is in Julia set)
  // Fail if we escaped early (unstable/suspicious behavior)
  const threshold = crypto.h.H;
  if (iterations >= threshold) {
    return VerificationResult.pass({ 
      iterations,
      z0: { real: z0_real, imag: z0_imag },
      c: { real: c_real, imag: c_imag }
    });
  } else {
    return VerificationResult.fail('fractal_rejected', {
      step: 'fractal',
      iterations,
      threshold
    });
  }
}

/**
 * Gate 3: Intent policy validation
 * Checks if intent is allowed for the specified provider
 */
function gate3_intentPolicy(envelope, policyConfig) {
  const { intent, aad } = envelope;
  
  // Check if provider is in policy
  if (!policyConfig || !policyConfig.providers) {
    return VerificationResult.fail('intent_policy_missing', {
      step: 'intent'
    });
  }
  
  const providerPolicy = policyConfig.providers[aad.route_hint];
  if (!providerPolicy) {
    return VerificationResult.fail('intent_provider_unknown', {
      step: 'intent',
      provider: aad.route_hint
    });
  }
  
  // Check if intent combination is allowed
  const intentKey = `${intent.primary}:${intent.modifier}`;
  if (!providerPolicy.allowed_intents.includes(intentKey)) {
    return VerificationResult.fail('intent_not_allowed', {
      step: 'intent',
      provider: aad.route_hint,
      intent: intentKey
    });
  }
  
  return VerificationResult.pass({ 
    provider: aad.route_hint,
    intent: intentKey
  });
}

/**
 * Gate 4: Trajectory window and phase lock
 * Validates time window and phase alignment
 */
function gate4_trajectoryPhase(envelope, currentTs = null) {
  const { trajectory, intent } = envelope;
  
  currentTs = currentTs || Math.floor(Date.now() / 1000);
  
  // Calculate current phase
  const currentPhase = calculateCurrentPhase(trajectory, currentTs);
  
  // Check phase alignment
  if (!isPhaseWithinTolerance(intent.phase_deg, currentPhase, 15)) {
    return VerificationResult.fail('trajectory_phase_misalign', {
      step: 'trajectory',
      expected_phase: intent.phase_deg,
      actual_phase: currentPhase,
      skew: Math.abs(intent.phase_deg - currentPhase)
    });
  }
  
  // Check if we're within the valid time window
  const elapsed = currentTs - trajectory.epoch;
  if (elapsed < 0) {
    return VerificationResult.fail('trajectory_too_early', {
      step: 'trajectory',
      current_ts: currentTs,
      epoch: trajectory.epoch
    });
  }
  
  return VerificationResult.pass({ 
    currentPhase,
    elapsed,
    phase_skew: Math.abs(intent.phase_deg - currentPhase)
  });
}

/**
 * Gate 5: Neural behavior energy
 * Computes energy metric from normalized context
 */
function gate5_neuralEnergy(envelope, energyConfig) {
  const { ctx } = envelope;
  
  // Normalize context values to [0,1] - already clamped
  const features = [
    ctx.entropy,
    ctx.server_load,
    ctx.stability,
    ctx.threat_level / 10  // Assume max threat level is 10
  ];
  
  // Compute energy as weighted sum (simple model)
  const weights = energyConfig?.weights || [1.0, 0.8, 0.6, 1.2];
  let energy = 0;
  for (let i = 0; i < features.length; i++) {
    energy += weights[i] * features[i] * features[i];
  }
  
  // Check against threshold
  const mu = energyConfig?.mean || 1.0;
  const sigma = energyConfig?.std || 0.3;
  const k = energyConfig?.k || 3.0;  // Number of standard deviations
  const threshold = mu + k * sigma;
  
  if (energy > threshold) {
    return VerificationResult.fail('neural_energy_high', {
      step: 'neural',
      energy,
      threshold
    });
  }
  
  // Check gradient margin (proximity to boundary)
  const epsilon = energyConfig?.epsilon || 0.1;
  const margin = threshold - energy;
  if (margin < epsilon) {
    return VerificationResult.fail('neural_boundary_proximity', {
      step: 'neural',
      energy,
      threshold,
      margin
    });
  }
  
  return VerificationResult.pass({ 
    energy,
    threshold,
    margin
  });
}

/**
 * Gate 6: Swarm trust validation
 * Validates agent/provider trust scores
 */
function gate6_swarmTrust(envelope, trustStore) {
  const { aad } = envelope;
  
  const provider = aad.route_hint;
  const providerTrust = trustStore.getTrust(provider);
  
  // Check provider trust threshold
  if (providerTrust < 0.3) {
    return VerificationResult.fail('swarm_trust_low', {
      step: 'swarm',
      provider,
      trust: providerTrust,
      threshold: 0.3
    });
  }
  
  // Check swarm entropy (diversity measure)
  const swarmEntropy = trustStore.getSwarmEntropy();
  if (swarmEntropy < 0.5) {
    return VerificationResult.fail('swarm_entropy_low', {
      step: 'swarm',
      entropy: swarmEntropy,
      threshold: 0.5
    });
  }
  
  return VerificationResult.pass({ 
    provider,
    trust: providerTrust,
    swarm_entropy: swarmEntropy
  });
}

/**
 * Run complete verification pipeline
 * Returns verification result or noise envelope if any gate fails
 */
async function runVerificationPipeline(envelope, config) {
  const results = {
    timestamp: Math.floor(Date.now() / 1000),
    gates: []
  };
  
  // Gate 1: Schema validation
  const schemaResult = gate1_schemaValidation(envelope);
  results.gates.push({ gate: 'schema', ...schemaResult });
  if (!schemaResult.passed) {
    return {
      success: false,
      reason: schemaResult.reason,
      results,
      noiseEnvelope: generateNoiseEnvelope(envelope)
    };
  }
  
  // Gate 2: Fractal gate
  const fractalResult = gate2_fractalGate(envelope);
  results.gates.push({ gate: 'fractal', ...fractalResult });
  if (!fractalResult.passed) {
    return {
      success: false,
      reason: fractalResult.reason,
      results,
      noiseEnvelope: generateNoiseEnvelope(envelope)
    };
  }
  
  // Gate 3: Intent policy
  if (config.intentPolicy) {
    const intentResult = gate3_intentPolicy(envelope, config.intentPolicy);
    results.gates.push({ gate: 'intent', ...intentResult });
    if (!intentResult.passed) {
      return {
        success: false,
        reason: intentResult.reason,
        results,
        noiseEnvelope: generateNoiseEnvelope(envelope)
      };
    }
  }
  
  // Gate 4: Trajectory and phase
  const trajectoryResult = gate4_trajectoryPhase(envelope, config.currentTs);
  results.gates.push({ gate: 'trajectory', ...trajectoryResult });
  if (!trajectoryResult.passed) {
    return {
      success: false,
      reason: trajectoryResult.reason,
      results,
      noiseEnvelope: generateNoiseEnvelope(envelope)
    };
  }
  
  // Gate 5: Neural energy
  if (config.energyConfig) {
    const neuralResult = gate5_neuralEnergy(envelope, config.energyConfig);
    results.gates.push({ gate: 'neural', ...neuralResult });
    if (!neuralResult.passed) {
      return {
        success: false,
        reason: neuralResult.reason,
        results,
        noiseEnvelope: generateNoiseEnvelope(envelope)
      };
    }
  }
  
  // Gate 6: Swarm trust
  if (config.trustStore) {
    const swarmResult = gate6_swarmTrust(envelope, config.trustStore);
    results.gates.push({ gate: 'swarm', ...swarmResult });
    if (!swarmResult.passed) {
      return {
        success: false,
        reason: swarmResult.reason,
        results,
        noiseEnvelope: generateNoiseEnvelope(envelope)
      };
    }
  }
  
  return {
    success: true,
    results
  };
}

/**
 * Generate noise envelope for failed verification
 */
function generateNoiseEnvelope(envelope) {
  const noise = generateDeterministicNoise(
    envelope.commit.ctx_sha256,
    envelope.crypto.salt_q_b64,
    4096,
    8192
  );
  return createNoiseResponse(envelope, noise);
}

module.exports = {
  VerificationResult,
  gate1_schemaValidation,
  gate2_fractalGate,
  gate3_intentPolicy,
  gate4_trajectoryPhase,
  gate5_neuralEnergy,
  gate6_swarmTrust,
  runVerificationPipeline,
  generateNoiseEnvelope
};
