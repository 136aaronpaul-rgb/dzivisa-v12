async function runAnyJS(code){
 const w=`self.onmessage=e=>{try{let r=eval(e.data);postMessage({ok:true,result:String(r)})}catch(err){postMessage({ok:false,error:err.message})}}`;
 const blob=new Blob([w],{type:"application/javascript"});
 const worker=new Worker(URL.createObjectURL(blob));
 return new Promise(res=>{
   worker.onmessage=m=>{res(m.data);worker.terminate();};
   worker.postMessage(code);
 });
}
