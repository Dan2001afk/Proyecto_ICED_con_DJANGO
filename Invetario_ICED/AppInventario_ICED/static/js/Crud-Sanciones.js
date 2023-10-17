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
        San_Pres_id: document.getElementById("San_Pres_id").value,
        San_tiempo: document.getElementById("San_tiempo").value,
        San_Descripcion: document.getElementById("San_Descripcion").value
    };
    var jsonData = JSON.stringify(Datos);

    fetch("http://127.0.0.1:8000/insertarSancion/",{
        method: "POST",
        body: jsonData,
        headers: {
            "Content-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        if (data.mensaje === "Datos Guardados") {
            ConsultarSanciones();
            mostrarCantidadEquipos();
            equiposInactivos
            Swal.fire({
                icon: 'success',
                title: '¡Éxito!',
                text: 'Datos enviados exitosamente.'
            });
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Error al enviar los datos.'
            });
        }
    })
    .catch(error => {
        console.error(error);
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Error al enviar los datos.'
        });
    });
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("FormSanciones").addEventListener("submit", function(event) {
        event.preventDefault();
        Agregar();
    });
});


//Buscar eliminar sancion 
function eliminarSancion(id_sancion) {
    const url = `http://127.0.0.1:8000/EliminarSancion/${id_sancion}`;

    Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta Acción Eliminará esta Sancion",
        icon: "error",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            fetch(url, {
                method: "DELETE",
                headers: {
                    "consultar-Type": "AppInventario_ICED/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                ConsultarSanciones();
                mostrarCantidadEquipos();
                equiposInactivos();
                
                Swal.fire("Éxito", "Sancion eliminadada exitosamente.", "success");
            })
            .catch(error => {
                console.error("Error al eliminar el La Sancion:", error);
                Swal.fire("Error", "Error al eliminar la Sancion.", "error");
            });
        }
    });
}

//Buscar sancion 
document.addEventListener("DOMContentLoaded", () => {
    const buscarSancionBtn = document.getElementById("BuscarSancion");
    buscarSancionBtn.addEventListener("click", () => {
        const sancionIdInput = document.getElementById("id_sancionn");
        const sancionId = sancionIdInput.value;

        if (sancionId) {
            const url = `http://127.0.0.1:8000/BuscarSancion/${sancionId}/`;

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
                if (sancion.hasOwnProperty('San_Id')) {
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                        <td>${sancion.San_Id}</td>
                        <td>${sancion.San_Pres_id}</td>
                        <td>${sancion.San_Fecha}</td>
                        <td>${sancion.San_Hora}</td>
                        <td>${sancion.San_tiempo}</td>
                        <td>${sancion.San_Descripcion}</td>
                        <td>
                            <div class="btn-container">
                                <button class="btnEliminar" onclick="eliminarSancion(${sancion.San_Id})">Eliminar</button>
                            </div>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                    
                } else {
                    Swal.fire({
                        title: "Sanción No Encontrada",
                        icon: "error", 
                        confirmButtonText: "Aceptar"
                    });
                    ConsultarSanciones();
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


function mostrarCantidadEquipos() {
    fetch("http://127.0.0.1:8000/ContarEquipos", {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        const cantidad = document.querySelector('.cantidad');

        
        // Actualizar los contadores con los datos obtenidos
        cantidad.textContent = `Total de equipos: ${data.cantidad_equipos}`;

    })
    .catch(error => {
        console.error("Error al obtener la cantidad de equipos:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    mostrarCantidadEquipos();
});


function equiposInactivos() {
    fetch("http://127.0.0.1:8000/ContarInactivos", {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        const inactivos = document.querySelector('.inactivos');

        
        // Actualizar los contadores con los datos obtenidos
        inactivos.textContent = `Total de equipos inactivos: ${data.cantidad_equipos_Inactivos}`;

    })
    .catch(error => {
        console.error("Error al obtener la cantidad de equipos inactivos:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    equiposInactivos();
});
