async function dzivisaLoadPlugin(url){
 try{ const m=await import(url); console.log("Loaded",url); return m; }
 catch(e){ console.log("Fail",url); return null; }
}
function dzivisaRunSafe(fn){ try{ fn(); } catch(e){ console.error(e.message); } }
