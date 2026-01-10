/**
 * SCBE (Secure Chaos-Based Encryption) Envelope System
 * Main entry point
 * 
 * @module @spiralverse/scbe-envelope
 * @version 2.0.0
 */

// Core components
const envelopeSchema = require('./core/envelope-schema');
const cryptoUtils = require('./core/crypto-utils');
const envelopeBuilder = require('./core/envelope-builder');

// Verification components
const pipeline = require('./verification/pipeline');
const trustStore = require('./verification/trust-store');

// Utilities
const metrics = require('./utils/metrics');

/**
 * Main SCBE API
 */
module.exports = {
  // Envelope creation
  buildEnvelope: envelopeBuilder.buildEnvelope,
  createNoiseResponse: envelopeBuilder.createNoiseResponse,
  addOrchestratorSignature: envelopeBuilder.addOrchestratorSignature,
  addProviderSignature: envelopeBuilder.addProviderSignature,

  // Validation
  validateEnvelope: envelopeSchema.validateEnvelope,
  verifyCommitHashes: cryptoUtils.verifyCommitHashes,

  // Verification pipeline
  runVerificationPipeline: pipeline.runVerificationPipeline,
  gate1_schemaValidation: pipeline.gate1_schemaValidation,
  gate2_fractalGate: pipeline.gate2_fractalGate,
  gate3_intentPolicy: pipeline.gate3_intentPolicy,
  gate4_trajectoryPhase: pipeline.gate4_trajectoryPhase,
  gate5_neuralEnergy: pipeline.gate5_neuralEnergy,
  gate6_swarmTrust: pipeline.gate6_swarmTrust,

  // Trust management
  TrustStore: trustStore.TrustStore,
  computeValidity: trustStore.computeValidity,

  // Cryptographic utilities
  canonicalize: cryptoUtils.canonicalize,
  sha256Hex: cryptoUtils.sha256Hex,
  sha256Object: cryptoUtils.sha256Object,
  computeCommitHashes: cryptoUtils.computeCommitHashes,
  generateQuerySalt: cryptoUtils.generateQuerySalt,
  generateDeterministicNoise: cryptoUtils.generateDeterministicNoise,
  computeDeterministicDelay: cryptoUtils.computeDeterministicDelay,

  // Phase utilities
  calculateCurrentPhase: envelopeBuilder.calculateCurrentPhase,
  isPhaseWithinTolerance: envelopeBuilder.isPhaseWithinTolerance,

  // Metrics
  metrics: metrics.globalMetrics,
  recordRejection: metrics.recordRejection,
  recordPhaseSkew: metrics.recordPhaseSkew,
  updateSwarmMetrics: metrics.updateSwarmMetrics,
  recordGFTScore: metrics.recordGFTScore,
  recordProviderCoherence: metrics.recordProviderCoherence,
  recordVerificationLatency: metrics.recordVerificationLatency,
  recordEnvelopeProcessed: metrics.recordEnvelopeProcessed,
  getMetricsSummary: metrics.getMetricsSummary,
  checkAlerts: metrics.checkAlerts,

  // Constants
  SCBE_VERSION: envelopeSchema.SCBE_VERSION
};
