const DZIVISA_LANGUAGES = {
  javascript: { name: "JavaScript", run: (code) => eval(code) },
  python: { name: "Python", cdn: "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js", loaded: false }
};

async function runPowerCode(lang, code) {
  if (lang === 'javascript') {
    return await runAnyJS(code);
  }
  if (lang === 'python') {
    if (!window.pyodide) {
      console.log("Loading Python 10MB...");
      const script = document.createElement('script');
      script.src = DZIVISA_LANGUAGES.python.cdn;
      document.head.appendChild(script);
      await new Promise(r => script.onload = r);
      window.pyodide = await loadPyodide();
      DZIVISA_LANGUAGES.python.loaded = true;
    }
    try {
      let result = await window.pyodide.runPythonAsync(code);
      return {ok: true, result: String(result)};
    } catch (e) {
      return {ok: false, error: e.message};
    }
  }
  return {ok:false, error: "Language not loaded yet"};
}
console.log("POWER engine ready: JS + Python");
