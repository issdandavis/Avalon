/**
 * SCBE Envelope Builder
 * Creates valid SCBE envelopes with proper validation and commit hashes
 */

const { validateEnvelope } = require('./envelope-schema');
const { computeCommitHashes, generateQuerySalt, sha256Object } = require('./crypto-utils');

/**
 * Build a complete SCBE envelope
 * 
 * @param {Object} params - Envelope parameters
 * @param {Object} params.ctx - Context object
 * @param {Object} params.intent - Intent object
 * @param {Object} params.trajectory - Trajectory object
 * @param {Object} params.aad - Additional Authenticated Data
 * @param {Object} params.crypto - Crypto configuration (partial)
 * @param {string} params.crypto.salt_q_b64 - Query salt (optional, will be generated if not provided)
 * @param {string} params.crypto.cipher_b64 - Ciphertext
 * @returns {Object} - Complete validated envelope
 */
function buildEnvelope(params) {
  const { ctx, intent, trajectory, aad, crypto } = params;

  // Generate query salt if not provided
  const salt_q_b64 = crypto.salt_q_b64 || generateQuerySalt(ctx, intent);

  // Build the envelope structure
  const envelope = {
    ver: 'scbe-2.0',
    ctx,
    intent,
    trajectory,
    aad,
    commit: {},
    crypto: {
      kem: 'ML-KEM-768',
      sig: 'ML-DSA-65',
      h: crypto.h || {
        d: 4,
        R: 1.5,
        H: Math.pow(1.5, 16),
        n_iter: 6500
      },
      salt_q_b64,
      cipher_b64: crypto.cipher_b64
    },
    sig: {
      orchestrator_sig_b64: null,
      provider_sig_b64: null
    }
  };

  // Compute and add commit hashes
  envelope.commit = computeCommitHashes(envelope);

  // Validate the complete envelope
  return validateEnvelope(envelope);
}

/**
 * Create a noise response (for rejection scenarios)
 * 
 * @param {Object} originalEnvelope - Original envelope that failed verification
 * @param {Buffer} noiseBuffer - Deterministic noise buffer
 * @returns {Object} - Envelope with noise ciphertext
 */
function createNoiseResponse(originalEnvelope, noiseBuffer) {
  return {
    ...originalEnvelope,
    crypto: {
      ...originalEnvelope.crypto,
      cipher_b64: noiseBuffer.toString('base64')
    },
    sig: {
      ...originalEnvelope.sig,
      provider_sig_b64: null
    }
  };
}

/**
 * Update envelope with orchestrator signature
 * 
 * @param {Object} envelope - Envelope to sign
 * @param {string} signature_b64 - Base64-encoded signature
 * @returns {Object} - Envelope with signature
 */
function addOrchestratorSignature(envelope, signature_b64) {
  return {
    ...envelope,
    sig: {
      ...envelope.sig,
      orchestrator_sig_b64: signature_b64
    }
  };
}

/**
 * Update envelope with provider signature (return path)
 * 
 * @param {Object} envelope - Envelope from provider
 * @param {string} signature_b64 - Base64-encoded provider signature
 * @returns {Object} - Envelope with provider signature
 */
function addProviderSignature(envelope, signature_b64) {
  return {
    ...envelope,
    sig: {
      ...envelope.sig,
      provider_sig_b64: signature_b64
    }
  };
}

/**
 * Calculate current phase angle from trajectory
 * 
 * @param {Object} trajectory - Trajectory object
 * @param {number} currentTs - Current timestamp (seconds)
 * @returns {number} - Phase angle in degrees (0-359)
 */
function calculateCurrentPhase(trajectory, currentTs) {
  const elapsed = currentTs - trajectory.epoch;
  const periods = elapsed / trajectory.period_s;
  const phaseRadians = (2 * Math.PI * periods) % (2 * Math.PI);
  const phaseDegrees = Math.floor((phaseRadians * 180 / Math.PI)) % 360;
  return phaseDegrees;
}

/**
 * Check if phase is within tolerance
 * 
 * @param {number} expectedPhase - Expected phase from intent
 * @param {number} actualPhase - Calculated actual phase
 * @param {number} tolerance - Tolerance in degrees (default 15)
 * @returns {boolean} - True if within tolerance
 */
function isPhaseWithinTolerance(expectedPhase, actualPhase, tolerance = 15) {
  // Handle wrap-around at 0/360 degrees
  let diff = Math.abs(expectedPhase - actualPhase);
  if (diff > 180) {
    diff = 360 - diff;
  }
  return diff <= tolerance;
}

module.exports = {
  buildEnvelope,
  createNoiseResponse,
  addOrchestratorSignature,
  addProviderSignature,
  calculateCurrentPhase,
  isPhaseWithinTolerance
};
