// Lightweight tracing module for Polly's Wingscroll HTML version
// Captures user path, stat evolution, and endings for analytics or AI agent review.

(function(){
  'use strict';
  
  const trace = {
    sessionId: Date.now().toString(36) + '-' + Math.random().toString(16).slice(2),
    startedAt: new Date().toISOString(),
    events: []
  };

  /**
   * Record a trace event with timestamp and metadata
   * @param {string} type - Event type identifier
   * @param {Object} payload - Event data and metadata
   */
  function traceEvent(type, payload) {
    if (!type) {
      console.warn('traceEvent called without type parameter');
      return;
    }
    
    trace.events.push({
      t: new Date().toISOString(),
      type,
      ...payload
    });
  }

  /**
   * Export complete trace data as JSON string
   * @returns {string} JSON representation of all trace events
   */
  function exportTrace() {
    return JSON.stringify(trace, null, 2);
  }

  /**
   * Clear all trace events and reset session start time
   */
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
