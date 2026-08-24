function reportScamToAaron(){
  const el=document.getElementById('msgBar');
  if(!el||!el.value.trim()){alert("Isa message kutanga!");return;}
  window.open(`https://wa.me/263788180242?text=${encodeURIComponent("🛡️ DZIVISA REPORT: "+el.value)}`,'_blank');
}
