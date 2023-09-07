// Listar equipos
function Consultar() {
    fetch("http://127.0.0.1:8000/ListarEquipos",{
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(datos => {
        console.log(datos);
        let tabla = document.querySelector('#tabla1-body');
        tabla.innerHTML = "";

        if (datos.length === 0) {
            tabla.innerHTML += `<tr> <td colspan="7"> no hay datos </td> </tr>`;
        } else {
            for (let dat of datos) {
                tabla.innerHTML += `
                <tr>
                <td>${dat.Equ_id}</td>
                <td>${dat.Equi_tipo}</td>
                <td>${dat.Equi_modelo}</td>
                <td>${dat.Equi_color}</td>
                <td>${dat.Equi_serial}</td>
                <td>${dat.Equi_estado}</td>
                <td>${dat.equi_especialidad}</td>
                <td>
                <div class="btn-container">
                <button class="btnEliminar" onclick="eliminarEquipo(${dat.Equ_id})">Eliminar</button>
                <button class="btnActualizar" onclick="capturarYActualizarEquipo(${dat.Equ_id})">Actualizar</button>
                </div>
                </td>
                </tr>`;

                            // Obtén todos los botones de "Actualizar"
                const updateButtons = document.querySelectorAll('.btnActualizar');
                
                // Agrega un evento de clic a cada botón de "Actualizar"
                updateButtons.forEach(button => {
                    button.addEventListener('click', function() {
                        const equipoId = button.getAttribute('data-equipo-id');
                        abrirModalActualizar(equipoId);
                    });
                });
            }
        }
    });
}

//Agregar equipo
function agregarEquipo() {
    var Equi_tipo = document.getElementById("Equi_tipo").value;
    var Equi_modelo = document.getElementById("Equi_modelo").value;
    var Equi_color = document.getElementById("Equi_color").value;
    var Equi_serial = document.getElementById("Equi_serial").value;
    var Equi_estado = document.getElementById("Equi_estado").value;
    var equi_especialidad = document.getElementById("equi_especialidad").value;

    if (
        Equi_tipo === "" ||
        Equi_modelo === "" ||
        Equi_color === "" ||
        Equi_serial === "" ||
        Equi_estado === "" ||
        equi_especialidad === ""
    ) {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Por favor, complete todos los campos."
        });
        return; // No envíes la solicitud si hay campos vacíos
    }

    var datos = {
        Equi_tipo: Equi_tipo,
        Equi_modelo: Equi_modelo,
        Equi_color: Equi_color,
        Equi_serial: Equi_serial,
        Equi_estado: Equi_estado,
        equi_especialidad: equi_especialidad
    };

    var jsonData = JSON.stringify(datos);

    fetch("http://127.0.0.1:8000/insertar/", {
        method: "POST",
        body: jsonData,
        headers: {
            "Content-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        Consultar();
        mostrarCantidadEquipos();
        Swal.fire({
            icon: "success",
            title: "Éxito",
            text: "Datos enviados exitosamente."
        });
    })
    .catch(error => {
        console.error(error);
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Serial ya existente"
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("FormEquipos").addEventListener("submit", function (event) {
        event.preventDefault();
        agregarEquipo();
    });
});

//Eliminar Equipo
function eliminarEquipo(Equ_id) {
    const url = `http://127.0.0.1:8000/EliminarEquipo/${Equ_id}`;

    Swal.fire({
        title: "¿Estás seguro?",
        text: "Esta Acción Eliminará El Equipo",
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
                Consultar();
                mostrarCantidadEquipos();
                Swal.fire("Éxito", "Registro eliminado exitosamente.", "success");
            })
            .catch(error => {
                console.error("Error al eliminar el equipo:", error);
                Swal.fire("Error", "Error al eliminar el equipo.", "error");
            });
        }
    });
}

//Buscar Equipo
document.addEventListener("DOMContentLoaded", () => {
    const buscarBtn = document.getElementById("BuscarEquipo");
    buscarBtn.addEventListener("click", () => {
        const equipoIdInput = document.getElementById("id_equipoo");
        const equipoId = equipoIdInput.value;

        if (equipoId) {
            const url = `http://127.0.0.1:8000/BuscarEquipo/${equipoId}`;

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
                    throw new Error("Error al buscar el equipo por ID");
                }
            })
            .then(equipo => {
                if (equipo.hasOwnProperty('Equ_id')) {
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                        <td>${equipo.Equ_id}</td>
                        <td>${equipo.Equi_tipo}</td>
                        <td>${equipo.Equi_modelo}</td>
                        <td>${equipo.Equi_color}</td>
                        <td>${equipo.Equi_serial}</td>
                        <td>${equipo.Equi_estado}</td>
                        <td>${equipo.equi_especialidad}</td>
                        <td>
                            <div class="btn-container">
                                <button class="btnEliminar" onclick="eliminarEquipo(${equipo.Equ_id})">Eliminar</button>
                                <button class="btnActualizar" data-equipo-id="${equipo.Equ_id}">Actualizar</button>
                            </div>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                    
                    // Agregar evento de clic al botón de "Actualizar"
                    const updateButton = newRow.querySelector('.btnActualizar');
                    updateButton.addEventListener('click', function() {
                        const equipoId = this.getAttribute('data-equipo-id');
                        abrirModalActualizar(equipoId);
                    });

                } else {
                    Swal.fire({
                        title: "Elemento No Encontrado",
                        icon: "error", 
                        confirmButtonText: "Aceptar"
                    });
                    Consultar();
                }
            })
            .catch(error => {
                console.error("Error al buscar el equipo por ID:", error);
                alert("Error al buscar el equipo por ID");
            });
        } else {
            console.error("Debe ingresar un ID de equipo válido");
        }
    });
});


//funciones adiccionales
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


//funcion para que el boton pueda abrir el modal desde JS
function abrirModalActualizar() {
    const updateModal = document.getElementById('myModal');
    updateModal.style.display = 'block'; // Muestra el modal de actualización
    
    const closeUpdateModalBtn = updateModal.querySelector('.close');
    closeUpdateModalBtn.addEventListener('click', function() {
        updateModal.style.display = 'none'; // Cierra el modal de actualización
    });

    closeUpdateModalBtn.addEventListener('mouseenter', function() {
        closeUpdateModalBtn.style.color = 'red'; // Cambia el color al pasar cerca del cursor
    });

    closeUpdateModalBtn.addEventListener('mouseleave', function() {
        closeUpdateModalBtn.style.color = '#aaa'; // Restaura el color original
    });

    // Aquí puedes realizar acciones adicionales según tus necesidades, como cargar los datos del equipo en el modal.
}


//funcion actualizar que atrapa datos del registro
function capturarYActualizarEquipo(equipoId) {
    fetch(`http://127.0.0.1:8000/BuscarEquipo/${equipoId}`, {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {
        // Populate the form fields with the retrieved data
        document.getElementById('Equ_id_Act').value = data.Equ_id;
        document.getElementById('Equi_tipo_Act').value = data.Equi_tipo;
        document.getElementById('Equi_modelo_Act').value = data.Equi_modelo;
        document.getElementById('Equi_color_Act').value = data.Equi_color;
        document.getElementById('Equi_serial_Act').value = data.Equi_serial;
        document.getElementById('Equi_estado_Act').value = data.Equi_estado;
        document.getElementById('equi_especialidad_Act').value = data.equi_especialidad;

        // Show the update form
        document.getElementById('ActualizarEquipos').style.display = 'block';
        
        // Update the form submission event listener
        document.getElementById("ActualizarEquipos").addEventListener("submit", function (event) {
            event.preventDefault();
            actualizarEquipo(equipoId);
        });
    });
}

function actualizarEquipo(Equ_id) {
    var datos = {
        Equ_id: document.getElementById("Equ_id_Act").value,
        Equi_tipo: document.getElementById("Equi_tipo_Act").value,
        Equi_modelo: document.getElementById("Equi_modelo_Act").value,
        Equi_color: document.getElementById("Equi_color_Act").value,
        Equi_serial: document.getElementById("Equi_serial_Act").value,
        Equi_estado: document.getElementById("Equi_estado_Act").value,
        equi_especialidad: document.getElementById("equi_especialidad_Act").value
    };

    var jsonData = JSON.stringify(datos);

    fetch("http://127.0.0.1:8000/ActualizarEquipo/" + Equ_id, {
        method: "POST", 
        body: jsonData,
        headers: {
            "Content-Type": "application/json" 
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        Consultar();
        Swal.fire({
            icon: "success",
            title: "Éxito",
            text: "Datos enviados exitosamente.",
        });

    })
    .catch(error => {
        console.error(error);
        Swal.fire({
            icon: "error",
            title: "Error",
            text: "Error al enviar los datos."
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    // Replace 'equipoId' with the actual ID of the equipment you want to capture and update
    capturarYActualizarEquipo(equipoId);
});