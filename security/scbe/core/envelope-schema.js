/**
 * SCBE Envelope Schema v2.0
 * Immutable envelope for gateway → orchestrator → providers
 * All verification inputs are deterministic and inside the envelope
 */

const crypto = require('crypto');

/**
 * SCBE Envelope Structure
 */
const SCBE_VERSION = 'scbe-2.0';

/**
 * Clamp a value between 0 and 1
 */
function clamp01(value) {
  return Math.max(0, Math.min(1, value));
}

/**
 * Validate and clamp context values
 */
function validateContext(ctx) {
  if (!ctx || typeof ctx !== 'object') {
    throw new Error('Context must be an object');
  }

  if (!Number.isInteger(ctx.ts) || ctx.ts <= 0) {
    throw new Error('Context ts must be a positive integer (seconds)');
  }

  if (!ctx.device_id || typeof ctx.device_id !== 'string') {
    throw new Error('Context device_id must be a non-empty string');
  }

  if (!Number.isInteger(ctx.threat_level) || ctx.threat_level < 0) {
    throw new Error('Context threat_level must be a non-negative integer');
  }

  return {
    ts: ctx.ts,
    device_id: ctx.device_id,
    threat_level: ctx.threat_level,
    entropy: clamp01(ctx.entropy || 0),
    server_load: clamp01(ctx.server_load || 0),
    stability: clamp01(ctx.stability || 0)
  };
}

/**
 * Validate intent structure
 */
function validateIntent(intent) {
  if (!intent || typeof intent !== 'object') {
    throw new Error('Intent must be an object');
  }

  if (!intent.primary || typeof intent.primary !== 'string') {
    throw new Error('Intent primary must be a non-empty string');
  }

  if (!intent.modifier || typeof intent.modifier !== 'string') {
    throw new Error('Intent modifier must be a non-empty string');
  }

  if (!Number.isInteger(intent.harmonic) || intent.harmonic < 1 || intent.harmonic > 7) {
    throw new Error('Intent harmonic must be an integer between 1 and 7');
  }

  if (!Number.isInteger(intent.phase_deg) || intent.phase_deg < 0 || intent.phase_deg > 359) {
    throw new Error('Intent phase_deg must be an integer between 0 and 359');
  }

  return {
    primary: intent.primary,
    modifier: intent.modifier,
    harmonic: intent.harmonic,
    phase_deg: intent.phase_deg
  };
}

/**
 * Validate trajectory structure
 */
function validateTrajectory(traj) {
  if (!traj || typeof traj !== 'object') {
    throw new Error('Trajectory must be an object');
  }

  if (!Number.isInteger(traj.epoch) || traj.epoch <= 0) {
    throw new Error('Trajectory epoch must be a positive integer');
  }

  if (!Number.isInteger(traj.period_s) || traj.period_s <= 0) {
    throw new Error('Trajectory period_s must be a positive integer');
  }

  if (!traj.slot_id || typeof traj.slot_id !== 'string') {
    throw new Error('Trajectory slot_id must be a non-empty string');
  }

  if (!Number.isInteger(traj.waypoint) || traj.waypoint < 0) {
    throw new Error('Trajectory waypoint must be a non-negative integer');
  }

  return {
    epoch: traj.epoch,
    period_s: traj.period_s,
    slot_id: traj.slot_id,
    waypoint: traj.waypoint
  };
}

/**
 * Validate AAD (Additional Authenticated Data) structure
 */
function validateAAD(aad) {
  if (!aad || typeof aad !== 'object') {
    throw new Error('AAD must be an object');
  }

  if (!aad.route_hint || typeof aad.route_hint !== 'string') {
    throw new Error('AAD route_hint must be a non-empty string');
  }

  return {
    route_hint: aad.route_hint,
    run_id: aad.run_id || null,
    step_no: aad.step_no || 0
  };
}

/**
 * Validate crypto structure
 */
function validateCrypto(crypto_data) {
  if (!crypto_data || typeof crypto_data !== 'object') {
    throw new Error('Crypto must be an object');
  }

  if (crypto_data.kem !== 'ML-KEM-768') {
    throw new Error('Crypto kem must be ML-KEM-768');
  }

  if (crypto_data.sig !== 'ML-DSA-65') {
    throw new Error('Crypto sig must be ML-DSA-65');
  }

  if (!crypto_data.h || typeof crypto_data.h !== 'object') {
    throw new Error('Crypto h (chaos parameters) must be an object');
  }

  if (!crypto_data.salt_q_b64 || typeof crypto_data.salt_q_b64 !== 'string') {
    throw new Error('Crypto salt_q_b64 must be a non-empty string');
  }

  if (!crypto_data.cipher_b64 || typeof crypto_data.cipher_b64 !== 'string') {
    throw new Error('Crypto cipher_b64 must be a non-empty string');
  }

  return {
    kem: crypto_data.kem,
    sig: crypto_data.sig,
    h: {
      d: crypto_data.h.d || 4,
      R: crypto_data.h.R || 1.5,
      H: crypto_data.h.H || Math.pow(1.5, 16),
      n_iter: crypto_data.h.n_iter || 6500
    },
    salt_q_b64: crypto_data.salt_q_b64,
    cipher_b64: crypto_data.cipher_b64
  };
}

/**
 * Validate complete SCBE envelope
 */
function validateEnvelope(envelope) {
  if (!envelope || typeof envelope !== 'object') {
    throw new Error('Envelope must be an object');
  }

  if (envelope.ver !== SCBE_VERSION) {
    throw new Error(`Envelope version must be ${SCBE_VERSION}`);
  }

  const validatedEnvelope = {
    ver: SCBE_VERSION,
    ctx: validateContext(envelope.ctx),
    intent: validateIntent(envelope.intent),
    trajectory: validateTrajectory(envelope.trajectory),
    aad: validateAAD(envelope.aad),
    commit: envelope.commit || {},
    crypto: validateCrypto(envelope.crypto),
    sig: envelope.sig || {
      orchestrator_sig_b64: null,
      provider_sig_b64: null
    }
  };

  return validatedEnvelope;
}

module.exports = {
  SCBE_VERSION,
  clamp01,
  validateContext,
  validateIntent,
  validateTrajectory,
  validateAAD,
  validateCrypto,
  validateEnvelope
};
