//LISTAR EQUIPOS
function Consultar() {
    fetch("http://127.0.0.1:8000/ListarEquipos",{
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
        <td>${dat.Equ_id}</td>
        <td>${dat.Equi_tipo}</td>
        <td>${dat.Equi_modelo}</td>
        <td>${dat.Equi_color}</td>
        <td>${dat.Equi_serial}</td>
        <td>${dat.Equi_estado}</td>
        <td>${dat.equi_especialidad}</td>
        </tr>`
    }
}

})

}

