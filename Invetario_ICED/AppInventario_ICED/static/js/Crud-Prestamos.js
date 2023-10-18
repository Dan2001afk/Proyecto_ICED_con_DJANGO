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
                <td>
                <div class="btn-container">
                <button class="btnEliminar" onclick="eliminarPrestamo(${dat.Pres_Id})">Liberar</button>
                </div>
                </td>
                </tr>`;
            }
        }
    });
}

//Agregar un Prestamo
function Agregar() {
    var Datos = {
        Pres_Equipos_serial: document.getElementById("Pres_Equipos_serial").value,
        Pres_Usuarios_Documento_id: document.getElementById("Pres_Usuarios_Documento_id").value,
        Pres_Tiempo_Limite: document.getElementById("Pres_Tiempo_Limite").value,
    };

    var jsonData = JSON.stringify(Datos);

    fetch("http://127.0.0.1:8000/verificarPrestamo/", {
        method: "POST",
        body: jsonData,
        headers: {
            "Content-Type": "application/json"
        }
    })
    .then(response => {
        if (response.status === 200) {
            return response.json();
        } else {
            throw new Error('Error en la solicitud.');
        }
    })
    .then(data => {
        if (data.error) {
            // Muestra SweetAlert con el mensaje de error recibido del servidor
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: data.error
            });
        } else {
            fetch("http://127.0.0.1:8000/insertarPrestamo/", {
                method: "POST",
                body: jsonData,
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    throw new Error('Error en la solicitud.');
                }
            })
            .then(data => {
                Listar();
                cantidadPrestamos();
                equiposEnPrestamo();
                // Muestra SweetAlert de éxito
                Swal.fire({
                    icon: 'success',
                    title: 'Éxito',
                    text: 'Datos enviados exitosamente.'
                });
            })
            .catch(error => {
                console.error(error);
                // Muestra SweetAlert de error al enviar los datos
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Error al enviar los datos'
                });
            });
        }
    })
    .catch(error => {
        console.error(error);
        // Muestra SweetAlert de error al verificar el préstamo
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Error al verificar el préstamo: ' + error.message
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("FormPrestamos").addEventListener("submit", function (event) {
        event.preventDefault();
        Agregar();
        cantidadPrestamos();
        equiposEnPrestamo();
        mostrarCantidadEquipos();
    });
});


//funcion para eliminar prestamo
function eliminarPrestamo(Pres_Id) {
    Swal.fire({
        title: "Devolucion del Dispositivo",
        icon: "question",
        showCancelButton: true,
        confirmButtonText: "Liberar Dispositivo",
        //cancelButtonText: "Realizar una sancion",
    }).then((result) => {
        if (result.isConfirmed) {
            const url = `http://127.0.0.1:8000/EliminarPrestamo/${Pres_Id}`;

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
                    equiposEnPrestamo();
                    mostrarCantidadEquipos();
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
    const buscarBtn = document.getElementById("BuscarPrestamo");
    buscarBtn.addEventListener("click", () => {
        const prestamoIdInput = document.getElementById("id_prestamoo");
        const prestamoId = prestamoIdInput.value;

        if (prestamoId) {
            const url = `http://127.0.0.1:8000/BuscarPrestamo/${prestamoId}`;

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
            .then(prestamo => {
                if (prestamo.hasOwnProperty('Pres_Id')) {
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                        <td>${prestamo.Pres_Id}</td>
                        <td>${prestamo.Pres_Equipos_id}</td>
                        <td>${prestamo.Pres_Usuarios_Documento_id}</td>
                        <td>${prestamo.Pres_Fec_Entrega}</td>
                        <td>${prestamo.Pres_Hora_Entrega}</td>
                        <td>${prestamo.Pres_Tiempo_Limite}</td>
                        <td>${prestamo.Pres_Observaciones_entrega}</td>
                        <td>
                            <div class="btn-container">
                                <button class="btnEliminar" onclick="eliminarPrestamo(${prestamo.Pres_Id})">Eliminar</button>
                            </div>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                    
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


function equiposEnPrestamo() {
    fetch("http://127.0.0.1:8000/contar_en_prestamo", {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        const enPrestamo = document.querySelector('.en-prestamo');

        // Actualizar los contadores con los datos obtenidos
        enPrestamo.textContent = `Total de equipos en préstamo: ${data.cantidad_equipos_en_prestamo}`;

    })
    .catch(error => {
        console.error("Error al obtener la cantidad de equipos en préstamo:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    equiposEnPrestamo();
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





