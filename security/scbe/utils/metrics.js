/**
 * SCBE Observability Metrics
 * Defines counters, gauges, and histograms for monitoring the SCBE system
 */

/**
 * Simple in-memory metrics store
 * In production, replace with Prometheus, StatsD, or similar
 */
class MetricsStore {
  constructor() {
    this.counters = new Map();
    this.gauges = new Map();
    this.histograms = new Map();
  }

  /**
   * Increment a counter
   */
  incrementCounter(name, labels = {}, value = 1) {
    const key = this._makeKey(name, labels);
    const current = this.counters.get(key) || 0;
    this.counters.set(key, current + value);
  }

  /**
   * Set a gauge value
   */
  setGauge(name, labels = {}, value) {
    const key = this._makeKey(name, labels);
    this.gauges.set(key, value);
  }

  /**
   * Record a histogram value
   */
  recordHistogram(name, labels = {}, value) {
    const key = this._makeKey(name, labels);
    if (!this.histograms.has(key)) {
      this.histograms.set(key, []);
    }
    this.histograms.get(key).push({
      timestamp: Date.now(),
      value
    });

    // Keep last 1000 values
    const hist = this.histograms.get(key);
    if (hist.length > 1000) {
      hist.shift();
    }
  }

  /**
   * Get counter value
   */
  getCounter(name, labels = {}) {
    const key = this._makeKey(name, labels);
    return this.counters.get(key) || 0;
  }

  /**
   * Get gauge value
   */
  getGauge(name, labels = {}) {
    const key = this._makeKey(name, labels);
    return this.gauges.get(key);
  }

  /**
   * Get histogram statistics
   */
  getHistogramStats(name, labels = {}) {
    const key = this._makeKey(name, labels);
    const values = (this.histograms.get(key) || []).map(v => v.value);
    
    if (values.length === 0) {
      return null;
    }

    values.sort((a, b) => a - b);
    
    return {
      count: values.length,
      min: values[0],
      max: values[values.length - 1],
      p50: values[Math.floor(values.length * 0.5)],
      p95: values[Math.floor(values.length * 0.95)],
      p99: values[Math.floor(values.length * 0.99)]
    };
  }

  /**
   * Create metric key from name and labels
   */
  _makeKey(name, labels) {
    const labelStr = Object.keys(labels)
      .sort()
      .map(k => `${k}=${labels[k]}`)
      .join(',');
    return labelStr ? `${name}{${labelStr}}` : name;
  }

  /**
   * Export all metrics
   */
  export() {
    return {
      counters: Object.fromEntries(this.counters),
      gauges: Object.fromEntries(this.gauges),
      histograms: Object.fromEntries(
        Array.from(this.histograms.entries()).map(([k, v]) => [
          k,
          this.getHistogramStats(k.split('{')[0], {})
        ])
      )
    };
  }

  /**
   * Reset all metrics
   */
  reset() {
    this.counters.clear();
    this.gauges.clear();
    this.histograms.clear();
  }
}

// Global metrics store singleton
const globalMetrics = new MetricsStore();

/**
 * SCBE-specific metric helpers
 */

/**
 * Record verification rejection
 */
function recordRejection(reason) {
  globalMetrics.incrementCounter('scbe.verify.reject_total', { reason });
}

/**
 * Record phase skew
 */
function recordPhaseSkew(skewDegrees) {
  globalMetrics.recordHistogram('scbe.phase.skew_deg', {}, skewDegrees);
}

/**
 * Update swarm trust metrics
 */
function updateSwarmMetrics(trustStore) {
  const avgTrust = trustStore.getAverageTrust();
  globalMetrics.setGauge('swarm.trust.avg', {}, avgTrust);

  // Per-agent trust
  for (const [agent, trust] of trustStore.trusts.entries()) {
    globalMetrics.setGauge('swarm.trust', { agent }, trust);
  }
}

/**
 * Record GFT rightshift score (spectral anomaly)
 */
function recordGFTScore(score) {
  globalMetrics.setGauge('gft.rightshift.score', {}, score);
}

/**
 * Record provider coherence
 */
function recordProviderCoherence(provider, coherence) {
  globalMetrics.setGauge('provider.coherence', { provider }, coherence);
}

/**
 * Record verification latency
 */
function recordVerificationLatency(durationMs) {
  globalMetrics.recordHistogram('scbe.verify.duration_ms', {}, durationMs);
}

/**
 * Record envelope processing
 */
function recordEnvelopeProcessed(success) {
  const status = success ? 'success' : 'failure';
  globalMetrics.incrementCounter('scbe.envelope.processed_total', { status });
}

/**
 * Get metrics summary for alerting
 */
function getMetricsSummary() {
  const phaseSkewStats = globalMetrics.getHistogramStats('scbe.phase.skew_deg', {});
  const avgTrust = globalMetrics.getGauge('swarm.trust.avg', {});
  const gftScore = globalMetrics.getGauge('gft.rightshift.score', {});

  return {
    phase_skew_p50: phaseSkewStats?.p50 || 0,
    phase_skew_p95: phaseSkewStats?.p95 || 0,
    swarm_trust_avg: avgTrust || 0,
    gft_rightshift_score: gftScore || 0,
    rejections: {
      fractal: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'fractal' }),
      intent: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'intent' }),
      trajectory: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'trajectory' }),
      phase: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'phase' }),
      neural: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'neural' }),
      swarm: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'swarm' }),
      sig: globalMetrics.getCounter('scbe.verify.reject_total', { reason: 'sig' })
    }
  };
}

/**
 * Check for alert conditions
 */
function checkAlerts(thresholds = {}) {
  const summary = getMetricsSummary();
  const alerts = [];

  // Check swarm trust
  if (summary.swarm_trust_avg < (thresholds.swarm_trust_avg || 0.5)) {
    alerts.push({
      severity: 'warning',
      metric: 'swarm.trust.avg',
      value: summary.swarm_trust_avg,
      threshold: thresholds.swarm_trust_avg || 0.5,
      message: 'Swarm average trust below threshold'
    });
  }

  // Check GFT score
  if (summary.gft_rightshift_score > (thresholds.gft_score || 0.8)) {
    alerts.push({
      severity: 'critical',
      metric: 'gft.rightshift.score',
      value: summary.gft_rightshift_score,
      threshold: thresholds.gft_score || 0.8,
      message: 'GFT rightshift score indicates spectral anomaly'
    });
  }

  // Check phase skew
  if (summary.phase_skew_p95 > (thresholds.phase_skew_p95 || 30)) {
    alerts.push({
      severity: 'warning',
      metric: 'scbe.phase.skew_deg_p95',
      value: summary.phase_skew_p95,
      threshold: thresholds.phase_skew_p95 || 30,
      message: 'Phase skew p95 indicates clock drift or replay attempts'
    });
  }

  return alerts;
}

module.exports = {
  MetricsStore,
  globalMetrics,
  recordRejection,
  recordPhaseSkew,
  updateSwarmMetrics,
  recordGFTScore,
  recordProviderCoherence,
  recordVerificationLatency,
  recordEnvelopeProcessed,
  getMetricsSummary,
  checkAlerts
};
