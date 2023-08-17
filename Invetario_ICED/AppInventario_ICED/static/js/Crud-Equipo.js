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
                <td><button class="btnEliminar" onclick="eliminarEquipo(${dat.Equ_id})">Eliminar</button></td>
                </tr>`;
            }
        }
    });
}

//Agregar equipo
function agregarEquipo() {
    var datos = {
        Equi_tipo: document.getElementById("Equi_tipo").value,
        Equi_modelo: document.getElementById("Equi_modelo").value,
        Equi_color: document.getElementById("Equi_color").value,
        Equi_serial: document.getElementById("Equi_serial").value,
        Equi_estado: document.getElementById("Equi_estado").value,
        equi_especialidad: document.getElementById("equi_especialidad").value
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
            text: "Error al enviar los datos."
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
        icon: "warning",
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
                        <td>Acciones</td>
                    `;

                    tablaBody.appendChild(newRow);
                } else {
                    alert("Equipo no registrado en la base de datos");
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





//Actualizar equipo
function actualizarEquipo(Equ_id_Actualizar) {
    var datos = {
        Equ_id_Actualizar: document.getElementById("Equ_id_Actualizar").value,
        Equi_tipo_Actualizar: document.getElementById("Equi_tipo_Actualizar").value,
        Equi_modelo_Actualizar: document.getElementById("Equi_modelo_Actualizar").value,
        Equi_color_Actualizar: document.getElementById("Equi_color_Actualizar").value,
        Equi_serial_Actualizar: document.getElementById("Equi_serial_Actualizar").value,
        Equi_estado_Actualizar: document.getElementById("Equi_estado_Actualizar").value,
        equi_especialidad_Actualizar: document.getElementById("equi_especialidad_Actualizar").value
    };

    var jsonData = JSON.stringify(datos);

    fetch("http://127.0.0.1:8000/ActualizarEquipo/" + Equ_id_Actualizar + "/", {
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
            text: "Error al enviar los datos."
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("ActualizarEquipos").addEventListener("submit", function (event) {
        event.preventDefault();
        var Equ_id_Actualizar = document.getElementById("Equ_id_Actualizar").value;
        actualizarEquipo(Equ_id_Actualizar);
    });
});