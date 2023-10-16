//Listar Historial de prestamos
function Listar(){
    fetch("http://127.0.0.1:8000/Listarhistorial",{
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
                <td>${dat.Pres_Usuarios_Documento_id}</td>
                <td>${dat.Pres_Equipos_id}</td>
                <td>${dat.Pres_Fec_Entrega}</td>
                <td>${dat.Pres_Hora_Entrega}</td>
                <td>${dat.Pres_Observaciones_entrega}</td>
                <td>
                <div class="btn-container">
                <button class="btnEliminar" onclick="eliminarHistorial(${dat.Pres_Id})">Eliminar</button>
                </div>
                </td>
                </tr>`;
            }
        }
    });
}

//funcion para eliminar prestamo
function eliminarHistorial(Pres_Id) {
    Swal.fire({
        title: "Esta accion eliminara el prestamo",
        icon: "error",
        showCancelButton: true,
        confirmButtonText: "Aceptar",
        cancelButtonText: "Cancelar",
    }).then((result) => {
        if (result.isConfirmed) {
            const url = `http://127.0.0.1:8000/EliminarHistorial/${Pres_Id}`;

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

//funcion Buscar Prestamo
document.addEventListener("DOMContentLoaded", () => {
    const buscarBtn = document.getElementById("BuscarHistorial");
    buscarBtn.addEventListener("click", () => {
        const historialIdInput = document.getElementById("id_historiall");
        const historialId = historialIdInput.value;

        if (historialId) {
            const url = `http://127.0.0.1:8000/BuscarHistorial/${historialId}`;

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
                    throw new Error("Error al buscar el Prestamo por ID");
                }
            })
            .then(historial => {
                if (historial.hasOwnProperty('Pres_Id')) {
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                        <td>${historial.Pres_Id}</td>
                        <td>${historial.Pres_Equipos_id}</td>
                        <td>${historial.Pres_Usuarios_Documento_id}</td>
                        <td>${historial.Pres_Fec_Entrega}</td>
                        <td>${historial.Pres_Hora_Entrega}</td>
                        <td>${historial.Pres_Tiempo_Limite}</td>
                        <td>${historial.Pres_Observaciones_entrega}</td>
                        <td>
                            <div class="btn-container">
                                <button class="btnEliminar" onclick="eliminarHistorial(${dat.Pres_Id})">Eliminar</button>
                                </div>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                    
                    // Agregar evento de clic al botón de "Actualizar"
                    const updateButton = newRow.querySelector('.btnActualizar');
                    updateButton.addEventListener('click', function() {
                        const prestamoId = this.getAttribute('data-prestamo-id');
                        abrirModalActualizar(historialId);
                    });

                } else {
                    Swal.fire({
                        title: "Elemento No Encontrado",
                        icon: "error", 
                        confirmButtonText: "Aceptar"
                    });
                    Listar();
                }
            })
            .catch(error => {
                console.error("Error al buscar el prestamo por ID:", error);
                alert("Error al buscar el prestamo por ID");
            });
        } else {
            console.error("Debe ingresar un ID de prestamo válido");
        }
    });
});

//funciones adicionales 
function cantidadPrestamos() {
    fetch("http://127.0.0.1:8000/ContarPrestamos", {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        const prestamos = document.querySelector('.prestamos');

        
        // Actualizar los contadores con los datos obtenidos
        prestamos.textContent = `Total de prestamos: ${data.cantidad_prestamos}`;

    })
    .catch(error => {
        console.error("Error al obtener la cantidad de prestamos:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    cantidadPrestamos();
});