/**
 * SCBE Cryptographic Utilities
 * Deterministic canonicalization and hash computation
 */

const crypto = require('crypto');

/**
 * Canonicalize an object for deterministic hashing
 * Sorts keys alphabetically to ensure consistency
 * 
 * @param {Object} obj - Object to canonicalize
 * @returns {string} - JSON string with sorted keys
 */
function canonicalize(obj) {
  if (obj === null || obj === undefined) {
    return JSON.stringify(obj);
  }

  if (typeof obj !== 'object') {
    return JSON.stringify(obj);
  }

  if (Array.isArray(obj)) {
    return JSON.stringify(obj.map(canonicalize).map(JSON.parse));
  }

  const sorted = {};
  Object.keys(obj).sort().forEach(key => {
    sorted[key] = obj[key];
  });

  return JSON.stringify(sorted, Object.keys(sorted).sort());
}

/**
 * Compute SHA-256 hash of a string
 * 
 * @param {string} str - String to hash
 * @returns {string} - Hex-encoded hash
 */
function sha256Hex(str) {
  return crypto.createHash('sha256').update(str, 'utf8').digest('hex');
}

/**
 * Compute SHA-256 hash of an object (via canonicalization)
 * 
 * @param {Object} obj - Object to hash
 * @returns {string} - Hex-encoded hash
 */
function sha256Object(obj) {
  const canonical = canonicalize(obj);
  return sha256Hex(canonical);
}

/**
 * Compute all commit hashes for an envelope
 * 
 * @param {Object} envelope - Partial envelope (ctx, intent, trajectory, aad)
 * @returns {Object} - Commit object with all hashes
 */
function computeCommitHashes(envelope) {
  return {
    ctx_sha256: sha256Object(envelope.ctx),
    intent_sha256: sha256Object(envelope.intent),
    traj_sha256: sha256Object(envelope.trajectory),
    aad_sha256: sha256Object(envelope.aad)
  };
}

/**
 * Verify that commit hashes match the envelope contents
 * 
 * @param {Object} envelope - Complete envelope with commit hashes
 * @returns {boolean} - True if all hashes match
 */
function verifyCommitHashes(envelope) {
  const computed = computeCommitHashes(envelope);
  
  return (
    envelope.commit.ctx_sha256 === computed.ctx_sha256 &&
    envelope.commit.intent_sha256 === computed.intent_sha256 &&
    envelope.commit.traj_sha256 === computed.traj_sha256 &&
    envelope.commit.aad_sha256 === computed.aad_sha256
  );
}

/**
 * Generate a deterministic per-query salt
 * 
 * @param {Object} ctx - Context object
 * @param {Object} intent - Intent object
 * @returns {string} - Base64-encoded salt
 */
function generateQuerySalt(ctx, intent) {
  const input = sha256Object(ctx) + sha256Object(intent);
  const salt = crypto.createHash('sha256').update(input).digest();
  return salt.toString('base64');
}

/**
 * Compute HMAC-SHA256
 * 
 * @param {string} key - HMAC key (can be string or Buffer)
 * @param {string} data - Data to MAC
 * @returns {Buffer} - HMAC output
 */
function hmacSha256(key, data) {
  return crypto.createHmac('sha256', key).update(data).digest();
}

/**
 * Generate deterministic noise for fail-to-noise responses
 * 
 * @param {string} ctx_sha256 - Context hash
 * @param {string} salt_q_b64 - Query salt
 * @param {number} minSize - Minimum noise size (default 4096)
 * @param {number} maxSize - Maximum noise size (default 8192)
 * @returns {Buffer} - Deterministic noise
 */
function generateDeterministicNoise(ctx_sha256, salt_q_b64, minSize = 4096, maxSize = 8192) {
  const seed = crypto.createHash('sha256')
    .update(ctx_sha256 + salt_q_b64)
    .digest();
  
  // Use seed to determine length within range
  const lengthRange = maxSize - minSize;
  const lengthOffset = seed.readUInt32BE(0) % lengthRange;
  const length = minSize + lengthOffset;
  
  // Generate deterministic noise using HMAC chain
  const noise = Buffer.alloc(length);
  let currentSeed = seed;
  
  for (let i = 0; i < length; i += 32) {
    currentSeed = hmacSha256(currentSeed, Buffer.from([i >> 8, i & 0xff]));
    currentSeed.copy(noise, i, 0, Math.min(32, length - i));
  }
  
  return noise;
}

/**
 * Compute deterministic delay jitter from hash
 * Used to normalize timing across error paths
 * 
 * @param {string} ctx_sha256 - Context hash
 * @param {number} baseDelayMs - Base delay in milliseconds
 * @param {number} jitterMs - Maximum jitter in milliseconds
 * @returns {number} - Deterministic delay in milliseconds
 */
function computeDeterministicDelay(ctx_sha256, baseDelayMs = 50, jitterMs = 50) {
  const hash = Buffer.from(ctx_sha256, 'hex');
  const jitterValue = hash.readUInt32BE(0) % jitterMs;
  return baseDelayMs + jitterValue;
}

module.exports = {
  canonicalize,
  sha256Hex,
  sha256Object,
  computeCommitHashes,
  verifyCommitHashes,
  generateQuerySalt,
  hmacSha256,
  generateDeterministicNoise,
  computeDeterministicDelay
};
