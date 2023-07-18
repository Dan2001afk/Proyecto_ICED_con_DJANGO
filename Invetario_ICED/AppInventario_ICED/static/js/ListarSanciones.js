//Listar Sanciones
function ConsultarSanciones(){
    fetch("http://127.0.0.1:8000/ListarSanciones",{
    method:"GET",
    headers:{
        "consultar-Type":"AppInventario_ICED/json"
    }
    })
    .then(Response => Response.json())
.then(datos=>{
console.log(datos)	
let tabla=document.querySelector('#tabla1-body');
tabla.innerHTML="";
if (datos==0) {
    tabla.innerHTML+=`<tr> <td> no hay datos </td> </tr>`
}
else{
    for (let dat of datos) {
        tabla.innerHTML+=`
        <tr>
        <td>${dat.San_Pres_id}</td>
        <td>${dat.San_Fecha}</td>
        <td>${dat.San_Hora}</td>
        <td>${dat.San_tiempo}</td>
        <td>${dat.San_Descripcion}</td>
        </tr>`
    }
}

})

}



