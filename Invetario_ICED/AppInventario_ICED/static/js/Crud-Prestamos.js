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
                <button class="btnActualizar" onclick="capturarYActualizarPrestamo(${dat.Pres_Id})">Actualizar</button>
                <button class="btnEliminar" onclick="eliminarPrestamo(${dat.Pres_Id})">Eliminar</button>
                </div>
                </td>
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

//Eliminar Prestamo
function eliminarPrestamo(prestamoId) {
    const url = `http://127.0.0.1:8000/EliminarPrestamo/${prestamoId}`;

    Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta Acción Eliminará El Prestamo",
        icon: "error",
        showCancelButton: true,
        confirmButtonText: "Aceptar",
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
                Listar(); 
                mostrarCantidadPrestamos();
                Swal.fire("Éxito", "Registro eliminado exitosamente.", "success");
            })
            .catch(error => {
                console.error("Error al eliminar el Prestamo:", error);
                Swal.fire("Error", "Error al eliminar el Prestamo.", "error");
            });
        }
    });
}

//Buscar Prestamo
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
                                <button class="btnActualizar" data-prestamo-id="${prestamo.Pres_Id}">Actualizar</button>
                            </div>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                    
                    // Agregar evento de clic al botón de "Actualizar"
                    const updateButton = newRow.querySelector('.btnActualizar');
                    updateButton.addEventListener('click', function() {
                        const prestamoId = this.getAttribute('data-prestamo-id');
                        abrirModalActualizar(prestamoId);
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

