//LISTAR PRESTAMOS
function ConsultarPrestamos() {
    fetch("http://127.0.0.1:8000/ListarPrestamos",{
        method:"GET",
        Headers:{
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
        <td>${dat.Pres_Id}</td>
        <td>${dat.Pres_Equipos_id}</td>
        <td>${dat.Pres_Usuarios_Documento_id}</td>
        <td>${dat.Pres_Fec_Entrega}</td>
        <td>${dat.Pres_Fec_Devolucion}</td>
        <td>${dat.Pres_Hora_Entrega}</td>
        <td>${dat.Pres_Hora_Devolucion}</td>
        <td>${dat.Pres_Tiempo_Limite}</td>
        <td>${dat.Pres_Observaciones_entrega}</td>
        <td>${dat.Pres_Observaciones_recibido}</td>
        </tr>`
    }
}
})
}
