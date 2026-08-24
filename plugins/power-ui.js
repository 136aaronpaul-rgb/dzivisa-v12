document.addEventListener("DOMContentLoaded", () => {
  // 1. Inject Neon Cyber Glow Styles safely into head
  const style = document.createElement("style");
  style.innerHTML = `
    body { transition: background 0.4s ease, box-shadow 0.4s ease; padding: 10px; background: #000 !important; }
    .clean-glow { box-shadow: inset 0 0 30px rgba(77,208,225,0.2) !important; border: 1px solid #4DD0E1 !important; }
    .danger-glow { box-shadow: inset 0 0 50px rgba(255,0,0,0.6) !important; border: 1px solid #ff0000 !important; animation: pulseGlow 1.5s infinite alternate !important; }
    @keyframes pulseGlow { from { box-shadow: inset 0 0 30px rgba(255,0,0,0.4); } to { box-shadow: inset 0 0 60px rgba(255,0,0,0.8); } }
    .metrics-card { background: #0a0f14; border: 1px solid #1a242f; border-radius: 8px; padding: 10px; margin-top: 10px; font-family: monospace; font-size: 11px; color: #4DD0E1; display: flex; justify-content: space-between; }
    .lang-select { width: 100%; background: #0f171e; color: #4DD0E1; border: 1px solid #4DD0E1; padding: 10px; border-radius: 8px; font-weight: bold; margin-bottom: 12px; }
  `;
  document.head.appendChild(style);
  document.body.classList.add("clean-glow");

  // 2. Inject Language Selector Dropdown at top of viewport
  const container = document.body;
  const selector = document.createElement("select");
  selector.className = "lang-select";
  selector.id = "globalLangSelector";
  
  Object.keys(DZIVISA_LOCALES).forEach(lang => {
    let opt = document.createElement("option");
    opt.value = lang;
    opt.innerText = `🌍 Language Mode: [${lang.toUpperCase()}]`;
    if(lang === "sn") opt.selected = true;
    selector.appendChild(opt);
  });
  container.insertBefore(selector, container.firstChild);

  // 3. Inject Cyber Performance Metrics Dashboard Layout Node
  const metricsBox = document.createElement("div");
  metricsBox.className = "metrics-card";
  metricsBox.id = "cyberMetricsDashboard";
  metricsBox.innerHTML = `<span>⏱️ ENGINE LATENCY: 0.00ms</span><span>🔍 VECTOR COUNT: 0/600</span>`;
  
  const msgBar = document.getElementById("msgBar");
  if(msgBar && msgBar.parentNode) {
    msgBar.parentNode.insertBefore(metricsBox, msgBar.nextSibling);
  }

  // 4. Hook interceptor directly onto scan loop sequences safely
  const originalScan = window.dzivisaScan;
  if (typeof originalScan === "function") {
    window.dzivisaScan = function(text) {
      const start = performance.now();
      const results = originalScan(text);
      const end = performance.now();
      const latency = (end - start).toFixed(2);
      
      const currentLang = document.getElementById("globalLangSelector")?.value || "sn";
      const loc = DZIVISA_LOCALES[currentLang];

      // Update Cyber Dashboard Nodes
      const dashboard = document.getElementById("cyberMetricsDashboard");
      if(dashboard) {
        let scannedCount = (results && results[0] && results[0].risk === "SAFE") ? 600 : "Short-Circuit";
        dashboard.innerHTML = `<span>⏱️ ${loc.speed.toUpperCase()}: ${latency}ms</span><span>🔍 RULES AUDITED: ${scannedCount}</span>`;
      }

      // Handle Live Visual Theme Mutation Glow Alerts
      if(results && results[0] && (results[0].risk === "CRITICAL" || results[0].risk === "HIGH")) {
        document.body.className = "danger-glow";
        results[0].title = `${loc.alert}: ${results[0].title.split(':').pop()}`;
        results[0].advice = loc.advice;
      } else {
        document.body.className = "clean-glow";
      }

      return results;
    };
  }
});
