// Listar Sanciones
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
            tabla.innerHTML += `<tr> <td colspan="7"> no hay datos </td> </tr>`;
        }
        else{
            for (let dat of datos) {
                tabla.innerHTML+=`
                <tr>
                <td>${dat.San_Id}</td>
                <td>${dat.San_Pres_id}</td>
                <td>${dat.San_Fecha}</td>
                <td>${dat.San_Hora}</td>
                <td>${dat.San_tiempo}</td>
                <td>${dat.San_Descripcion}</td>
                <td><button class="btnEliminar" onclick="eliminarSancion(${dat.San_Id})">Eliminar</button></td>
                </tr>`;
            }
        }
   });
}

//Agregar Sancion
function Agregar() {
    var Datos={
        San_Pres_id:document.getElementById("San_Pres_id").value,
        San_Fecha:document.getElementById("San_Fecha").value,
        San_Hora:document.getElementById("San_Hora").value,
        San_tiempo:document.getElementById("San_tiempo").value,
        San_Descripcion:document.getElementById("San_Descripcion").value
    };
    var jsonData=JSON.stringify(Datos);
    console.log(jsonData)
    fetch("http://127.0.0.1:8000/insertarSancion/",{
        method:"POST",
        body:jsonData,
        headers:{
            "Content-Type":"AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        ConsultarSanciones();
        alert("Datos enviados exitosamente.");
    })
    .catch(error => {
        console.error(error);
        alert("Error al enviar los datos.");
    });
}
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormSanciones").addEventListener("submit",function(event) {
        event.preventDefault();
        Agregar();
    });
});



//Eliminar Sancion
function eliminarSancion(sancionId) {
    const url = `http://127.0.0.1:8000/EliminarSancion/${sancionId}`;

    fetch(url, {
        method: "DELETE",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        ConsultarSanciones(); 
    })
    .catch(error => {
        console.error("Error al eliminar la Sancion:", error);
    });
}

