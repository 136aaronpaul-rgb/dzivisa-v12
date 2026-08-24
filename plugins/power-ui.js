document.addEventListener("DOMContentLoaded", () => {
  // 1. Inject Neon Cyber Glow Styles safely into head
  const style = document.createElement("style");
  style.innerHTML = `
    body { transition: background 0.4s ease, box-shadow 0.4s ease; padding: 10px; background: #000 !important; }
    .clean-glow { box-shadow: inset 0 0 30px rgba(77,208,225,0.2) !important; border: 1px solid #4DD0E1 !important; }
    .danger-glow { box-shadow: inset 0 0 50px rgba(255,0,0,0.6) !important; border: 1px solid #ff0000 !important; animation: pulseGlow 1.5s infinite alternate !important; }
    @keyframes pulseGlow { from { box-shadow: inset 0 0 30px rgba(255,0,0,0.4); } to { box-shadow: inset 0 0 60px rgba(255,0,0,0.8); } }
    .metrics-card { background: #0a0f14; border: 1px solid #1a242f; border-radius: 8px; padding: 10px; margin-top: 10px; font-family: monospace; font-size: 11px; color: #4DD0E1; display: flex; flex-direction: column; gap: 4px; }
    .metrics-row { display: flex; justify-content: space-between; width: 100%; }
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
  metricsBox.innerHTML = `
    <div class="metrics-row"><span>⏱️ ENGINE LATENCY: 0.00ms</span><span>🔍 VECTOR COUNT: 0/600</span></div>
    <div class="metrics-row" id="heuristicAnalyticsRow" style="color: #FFD700; border-top: 1px solid #1a242f; padding-top: 4px; margin-top: 2px;">📋 HEURISTICS: STANDBY</div>
  `;
  
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
      const analyticsRow = document.getElementById("heuristicAnalyticsRow");
      if(dashboard && results && results[0]) {
        let scannedCount = results[0].risk === "SAFE" ? 600 : "Short-Circuit";
        dashboard.querySelector(".metrics-row").innerHTML = `<span>⏱️ ${loc.speed.toUpperCase()}: ${latency}ms</span><span>🔍 RULES AUDITED: ${scannedCount}</span>`;
        if(analyticsRow) {
          analyticsRow.innerText = results[0].analytics || "📋 HEURISTICS: CLEAN";
        }
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

  // 5. CLIPBOARD LIVE-SNIFFER INTELLIGENCE INTEGRATION
  window.addEventListener('focus', async () => {
    try {
      if (!navigator.clipboard) return;
      const text = await navigator.clipboard.readText();
      if (text && text.trim().length > 10) {
        const msgBar = document.getElementById("msgBar");
        if (msgBar && msgBar.value !== text) {
          msgBar.value = text;
          console.log("⚡ Auto-Sniffed clip string. Executing heuristic evaluation loop...");
          if (typeof doScan === "function") {
            doScan();
          } else if (typeof window.dzivisaScan === "function") {
            window.dzivisaScan(text);
          }
        }
      }
    } catch (err) {
      console.log("📋 Clipboard auto-scan permissions waiting for active user event handler interaction.");
    }
  });
});
