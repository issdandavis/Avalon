// Lightweight tracing module for Polly's Wingscroll HTML version
// Captures user path, stat evolution, and endings for analytics or AI agent review.

(function(){
  const trace = {
    sessionId: Date.now().toString(36) + '-' + Math.random().toString(16).slice(2),
    startedAt: new Date().toISOString(),
    events: [],
    performance: {
      nodeRenderTimes: [],
      avgRenderTime: 0
    }
  };

  function traceEvent(type, payload) {
    trace.events.push({
      t: new Date().toISOString(),
      type,
      ...payload
    });
  }

  // Performance monitoring helper
  function measurePerformance(label, fn) {
    const start = performance.now();
    const result = fn();
    const end = performance.now();
    const duration = end - start;
    
    if (label === 'node_render') {
      trace.performance.nodeRenderTimes.push(duration);
      // Keep only last 50 render times
      if (trace.performance.nodeRenderTimes.length > 50) {
        trace.performance.nodeRenderTimes.shift();
      }
      // Update average
      trace.performance.avgRenderTime = 
        trace.performance.nodeRenderTimes.reduce((a, b) => a + b, 0) / 
        trace.performance.nodeRenderTimes.length;
    }
    
    return result;
  }

  function exportTrace() {
    return JSON.stringify(trace, null, 2);
  }

  function clearTrace() {
    trace.events.length = 0;
    trace.performance.nodeRenderTimes.length = 0;
    trace.performance.avgRenderTime = 0;
    trace.startedAt = new Date().toISOString();
    traceEvent('trace_reset', {});
  }

  function getPerformanceStats() {
    return {
      avgRenderTime: trace.performance.avgRenderTime.toFixed(2) + 'ms',
      sampleCount: trace.performance.nodeRenderTimes.length,
      totalEvents: trace.events.length
    };
  }

  // Expose globally
  window.gameTrace = trace;
  window.traceEvent = traceEvent;
  window.measurePerformance = measurePerformance;
  window.exportTrace = exportTrace;
  window.clearTrace = clearTrace;
  window.getPerformanceStats = getPerformanceStats;
})();
