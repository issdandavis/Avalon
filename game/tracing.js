// Lightweight tracing module for Polly's Wingscroll HTML version
// Captures user path, stat evolution, and endings for analytics or AI agent review.

(function(){
  const trace = {
    sessionId: Date.now().toString(36) + '-' + Math.random().toString(16).slice(2),
    startedAt: new Date().toISOString(),
    events: []
  };

  function traceEvent(type, payload) {
    trace.events.push({
      t: new Date().toISOString(),
      type,
      ...payload
    });
  }

  function exportTrace() {
    return JSON.stringify(trace, null, 2);
  }

  function clearTrace() {
    trace.events.length = 0;
    trace.startedAt = new Date().toISOString();
    traceEvent('trace_reset', {});
  }

  // Expose globally
  window.gameTrace = trace;
  window.traceEvent = traceEvent;
  window.exportTrace = exportTrace;
  window.clearTrace = clearTrace;
})();
