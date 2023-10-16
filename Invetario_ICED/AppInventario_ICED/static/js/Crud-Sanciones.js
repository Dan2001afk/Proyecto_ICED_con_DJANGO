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


function eliminarPrestamo(sancionId) {
    Swal.fire({
        title: "Devolucion del Dispositivo",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Liberar Dispositivo",
        cancelButtonText: "Realizar una sancion",
    }).then((result) => {
        if (result.isConfirmed) {
            const url = `http://127.0.0.1:8000/EliminarSancion/${sancionId}`;

            fetch(url, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json",
                },
            })
                .then((response) => {
                    if (response.ok) {
                        return response.json();
                    } else {
                        throw new Error("Error al eliminar el préstamo");
                    }
                })
                .then((data) => {
                    console.log(data);
                    Listar();
                    cantidadPrestamos();
                    Swal.fire({
                        title: "Préstamo eliminado exitosamente.",
                        icon: "success",
                    });
                })
                .catch((error) => {
                    console.error("Error al eliminar el préstamo:", error);
                    Swal.fire({
                        title: "Error al eliminar el préstamo",
                        text: error.message,
                        icon: "error",
                    });
                });
        }
    });
}



document.addEventListener("DOMContentLoaded", () => {
    const buscarBtn = document.getElementById("BuscarSancion");
    buscarBtn.addEventListener("click", () => {
        const sancionIdInput = document.getElementById("id_sancionn");
        const sancionId = sancionIdInput.value;

        if (sancionId) {
            const url = `http://127.0.0.1:8000/BuscarSancion/${sancionId}`;

            fetch(url, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error("Error al buscar la Sanción por ID");
                }
            })
            .then(sancion => {
                if (sancion.length > 0) {  // Comprobamos si se encontraron sanciones
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    sancion.forEach(sancion => {
                        const newRow = document.createElement("tr");
                        newRow.innerHTML = `
                            <td>${sancion.fields.San_Id}</td>
                            <td>${sancion.fields.San_Pres}</td>
                            <td>${sancion.fields.San_Fecha}</td>
                            <td>${sancion.fields.San_Hora}</td>
                            <td>${sancion.fields.San_tiempo}</td>
                            <td>${sancion.fields.San_Descripcion}</td>
                            <td>
                                <div class="btn-container">
                                    <button class="btnEliminar" onclick="eliminarSancion(${sancion.pk})">Eliminar</button>
                                </div>
                            </td>
                        `;

                        tablaBody.appendChild(newRow);
                    });
                } else {
                    Swal.fire({
                        title: "Elemento No Encontrado",
                        icon: "error", 
                        confirmButtonText: "Aceptar"
                    });
                }
            })
            .catch(error => {
                console.error("Error al buscar la sanción por ID:", error);
                alert("Error al buscar la sanción por ID");
            });
        } else {
            console.error("Debe ingresar un ID de sanción válido");
        }
    });
});
