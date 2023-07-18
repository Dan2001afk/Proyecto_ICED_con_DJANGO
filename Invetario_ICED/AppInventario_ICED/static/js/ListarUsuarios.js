//Listar Usuarios
function Consultar(){
    fetch("http://127.0.0.1:8000/ListarUsuarios",{
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
        <td>${dat.Usu_Documento}</td>
        <td>${dat.Usu_Nombre}</td>
        <td>${dat.Usu_Apellido}</td>
        <td>${dat.Usu_tipo}</td>
        <td>${dat.Usu_Celular}</td>
        <td>${dat.Usu_Correo}</td>
        <td>${dat.Usu_Ficha}</td>
        </tr>`
    }
}

})

}
