/**
 * Polly's Wingscroll: The First Thread
 * Gameplay Tracing Module
 * 
 * Copyright (c) 2025 Avalon Codex Authors
 * Licensed under MIT License (see LICENSE file)
 * 
 * Lightweight tracing module for capturing user paths, stat evolution,
 * and endings for analytics and development review.
 */

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
