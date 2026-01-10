/**
 * SCBE Trust Store
 * Manages trust scores for providers and agents with decay and self-exclusion
 */

/**
 * Trust Store for managing provider/agent trust scores
 */
class TrustStore {
  constructor() {
    this.trusts = new Map();  // provider -> trust score [0,1]
    this.history = new Map();  // provider -> array of validity scores
    this.alpha = 0.9;  // Decay factor (higher = slower decay)
    this.excludeThreshold = 0.3;
  }

  /**
   * Initialize trust for a provider
   */
  initialize(provider, initialTrust = 0.5) {
    if (!this.trusts.has(provider)) {
      this.trusts.set(provider, initialTrust);
      this.history.set(provider, []);
    }
  }

  /**
   * Get current trust score for a provider
   */
  getTrust(provider) {
    if (!this.trusts.has(provider)) {
      this.initialize(provider);
    }
    return this.trusts.get(provider);
  }

  /**
   * Update trust based on validity metric
   * validity: 0 = complete failure, 1 = perfect behavior
   */
  updateTrust(provider, validity) {
    this.initialize(provider);
    
    const currentTrust = this.trusts.get(provider);
    const newTrust = this.alpha * currentTrust + (1 - this.alpha) * validity;
    
    this.trusts.set(provider, newTrust);
    
    // Store in history
    const hist = this.history.get(provider);
    hist.push({ timestamp: Date.now(), validity, trust: newTrust });
    
    // Keep last 100 entries
    if (hist.length > 100) {
      hist.shift();
    }
    
    return newTrust;
  }

  /**
   * Check if provider should be excluded
   */
  shouldExclude(provider) {
    const trust = this.getTrust(provider);
    return trust < this.excludeThreshold;
  }

  /**
   * Get list of excluded providers
   */
  getExcluded() {
    const excluded = [];
    for (const [provider, trust] of this.trusts.entries()) {
      if (trust < this.excludeThreshold) {
        excluded.push(provider);
      }
    }
    return excluded;
  }

  /**
   * Compute swarm entropy (diversity measure)
   * Returns value in [0,1], higher is better (more diverse)
   */
  getSwarmEntropy() {
    const providers = Array.from(this.trusts.keys());
    if (providers.length === 0) {
      return 0;
    }
    
    // Normalize trust scores to probabilities
    const totalTrust = Array.from(this.trusts.values()).reduce((sum, t) => sum + t, 0);
    if (totalTrust === 0) {
      return 0;
    }
    
    // Compute Shannon entropy
    let entropy = 0;
    for (const trust of this.trusts.values()) {
      const p = trust / totalTrust;
      if (p > 0) {
        entropy -= p * Math.log2(p);
      }
    }
    
    // Normalize by max possible entropy
    const maxEntropy = Math.log2(providers.length);
    return maxEntropy > 0 ? entropy / maxEntropy : 0;
  }

  /**
   * Get average trust across all providers
   */
  getAverageTrust() {
    const trusts = Array.from(this.trusts.values());
    if (trusts.length === 0) {
      return 0;
    }
    return trusts.reduce((sum, t) => sum + t, 0) / trusts.length;
  }

  /**
   * Decay all trust scores (periodic maintenance)
   * Simulates natural trust erosion without positive reinforcement
   */
  applyGlobalDecay(decayFactor = 0.95) {
    for (const [provider, trust] of this.trusts.entries()) {
      this.trusts.set(provider, trust * decayFactor);
    }
  }

  /**
   * Get trust history for a provider
   */
  getHistory(provider) {
    return this.history.get(provider) || [];
  }

  /**
   * Export trust store state (for persistence)
   */
  export() {
    return {
      trusts: Object.fromEntries(this.trusts),
      alpha: this.alpha,
      excludeThreshold: this.excludeThreshold
    };
  }

  /**
   * Import trust store state (from persistence)
   */
  import(state) {
    this.trusts = new Map(Object.entries(state.trusts || {}));
    this.alpha = state.alpha || 0.9;
    this.excludeThreshold = state.excludeThreshold || 0.3;
  }
}

/**
 * Compute validity score for trust update
 * Combines multiple factors: neural pass, coherence, deviation penalty
 */
function computeValidity(checks) {
  const {
    neuralPassed = true,
    coherence = 1.0,  // [0,1]
    deviationPenalty = 0  // [0,1], higher is worse
  } = checks;

  const neuralScore = neuralPassed ? 1.0 : 0.0;
  const deviationScore = 1.0 - deviationPenalty;

  // Weighted combination
  const validity = 0.4 * neuralScore + 0.4 * coherence + 0.2 * deviationScore;

  return Math.max(0, Math.min(1, validity));
}

module.exports = {
  TrustStore,
  computeValidity
};
