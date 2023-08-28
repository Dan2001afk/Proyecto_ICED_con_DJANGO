//Listar Prestamos
function Listar(){
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
            tabla.innerHTML += `<tr> <td colspan="7"> no hay datos </td> </tr>`;
        }
        else{
            for (let dat of datos) {
                tabla.innerHTML+=`
                <tr>
                <td>${dat.Pres_Id}</td>
                <td>${dat.Pres_Equipos_id}</td>
                <td>${dat.Pres_Usuarios_Documento_id}</td>
                <td>${dat.Pres_Fec_Entrega}</td>
                <td>${dat.Pres_Hora_Entrega}</td>
                <td>${dat.Pres_Tiempo_Limite}</td>
                <td>${dat.Pres_Observaciones_entrega}</td>
                <td><button class="btnEliminar" onclick="eliminarPrestamo(${dat.Pres_Id})">Eliminar</button></td>
                </tr>`;
            }
        }
    });
}

//Agregar un Prestamo
function Agregar(){
    var Datos={
        Pres_Equipos_id:document.getElementById("Pres_Equipos_id").value,
        Pres_Usuarios_Documento_id:document.getElementById("Pres_Usuarios_Documento_id").value,
        Pres_Tiempo_Limite:document.getElementById("Pres_Tiempo_Limite").value,
        Pres_Observaciones_entrega:document.getElementById("Pres_Observaciones_entrega").value
    };

    var jsonData=JSON.stringify(Datos);
    console.log(jsonData)

    fetch("http://127.0.0.1:8000/insertarPrestamo/",{
        method:"POST",
        body: jsonData,
        headers:{
            "Content-Type":"AppInventario_ICED/json"
        }
    
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        Listar();
        alert("Datos enviados exitosamente.");
    })
    .catch(error => {
        console.error(error);
        alert("Error al enviar los datos.");
    });
}
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormPrestamos").addEventListener("submit",function(event) {
        event.preventDefault();
        Agregar();
    });
});

//Eliminar Equipo
function eliminarPrestamo(prestamoId) {
    const url = `http://127.0.0.1:8000/EliminarPrestamo/${prestamoId}`;

    fetch(url, {
        method: "DELETE",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        Listar(); 
    })
    .catch(error => {
        console.error("Error al eliminar el Prestamo:", error);
    });
}


