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
            tabla.innerHTML += `<tr> <td colspan="7"> no hay datos </td> </tr>`;
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
                <td><button class="btnEliminar" onclick="eliminarUsuario(${dat.Usu_Documento})">Eliminar</button></td>
                </tr>`;
            }
        }
    });
}

//Agregar Usuario
function Agregar(){
    var Datos={
        Usu_Documento:document.getElementById("Usu_Documento").value,
        Usu_Nombre:document.getElementById("Usu_Nombre").value,
        Usu_Apellido:document.getElementById("Usu_Apellido").value,
        Usu_tipo:document.getElementById("Usu_tipo").value,
        Usu_Celular:document.getElementById("Usu_Celular").value,
        Usu_Correo:document.getElementById("Usu_Correo").value,
        Usu_Ficha:document.getElementById("Usu_Ficha").value
    };

    var jsonData=JSON.stringify(Datos);
    console.log(jsonData);

    fetch("http://127.0.0.1:8000/insertarUsuario/",{
        method:"POST",
        body:jsonData,
        headers:{
            "Content-Type":"AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        Consultar();
        alert("Datos enviados exitosamente.");
    })
    .catch(error => {
        console.error(error);
        alert("Error al enviar los datos.");
    });
}

document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormUsuarios").addEventListener("submit",function(event) {
        event.preventDefault();
        Agregar();
    });
});

//Eliminar Usuario
function eliminarUsuario(Usu_Documento) {
    const url = `http://127.0.0.1:8000/EliminarUsuario/${Usu_Documento}`;

    fetch(url, {
        method: "DELETE",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        Consultar(); 
    })
    .catch(error => {
        console.error("Error al eliminar el Usuario:", error);
    });
}
