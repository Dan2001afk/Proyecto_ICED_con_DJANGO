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
function Agregar() {
    var Datos = {
        Usu_Documento: document.getElementById("Usu_Documento").value,
        Usu_Nombre: document.getElementById("Usu_Nombre").value,
        Usu_Apellido: document.getElementById("Usu_Apellido").value,
        Usu_tipo: document.getElementById("Usu_tipo").value,
        Usu_Celular: document.getElementById("Usu_Celular").value,
        Usu_Correo: document.getElementById("Usu_Correo").value,
        Usu_Ficha: document.getElementById("Usu_Ficha").value
    };

    var jsonData = JSON.stringify(Datos);
    console.log(jsonData);

    fetch("http://127.0.0.1:8000/insertarUsuario/", {
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

            // SweetAlert para éxito
            Swal.fire({
                title: "Éxito",
                text: "Datos enviados exitosamente.",
                icon: "success",
                confirmButtonText: "Aceptar"
            });
        })
        .catch(error => {
            console.error(error);

            // SweetAlert para error
            Swal.fire({
                title: "Error",
                text: "Error al enviar los datos.",
                icon: "error",
                confirmButtonText: "Aceptar"
            });
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

    // Mostrar un SweetAlert de confirmación
    Swal.fire({
        title: "Confirmar",
        text: "¿Está seguro de eliminar este usuario?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Eliminar",
        cancelButtonText: "Cancelar"
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la petición de eliminación si el usuario confirma
            fetch(url, {
                method: "DELETE",
                headers: {
                    "consultar-Type": "AppInventario_ICED/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                // Mostrar SweetAlert de éxito después de eliminar
                Swal.fire({
                    title: "Éxito",
                    text: "Usuario eliminado correctamente.",
                    icon: "success",
                    confirmButtonText: "Aceptar"
                });

                Consultar();
            })
            .catch(error => {
                console.error("Error al eliminar el Usuario:", error);
            });
        }
    });
}

// Actualizar usuario
function actualizarUsuario() {
    var datos = {
        Usu_Documento: document.getElementById("Usu_DocumentoActualizar").value,
        Usu_Nombre: document.getElementById("Usu_NombreActualizar").value,
        Usu_Apellido: document.getElementById("Usu_ApellidoActualizar").value,
        Usu_tipo: document.getElementById("Usu_tipoActualizar").value,
        Usu_Celular: document.getElementById("Usu_CelularActualizar").value,
        Usu_Correo: document.getElementById("Usu_CorreoActualizar").value,
        Usu_Ficha: document.getElementById("Usu_FichaActualizar").value
    };

    var jsonData = JSON.stringify(datos);

    fetch("http://127.0.0.1:8000/ActualizarUsuario/" + datos.Usu_Documento, {
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
    document.getElementById("ActualizarUsuarioForm").addEventListener("submit", function (event) {
        event.preventDefault();
        actualizarUsuario();
    });
});

//Buscar usuario

document.addEventListener("DOMContentLoaded", () => {
    const buscarBtn = document.getElementById("BuscarUsuario");
    buscarBtn.addEventListener("click", () => {
        const usuarioIdInput = document.getElementById("id_usuarioo");
        const usuarioId = usuarioIdInput.value;

        if (usuarioId) {
            const url = `http://127.0.0.1:8000/BuscarUsuario/${usuarioId}`;

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
                    throw new Error("Error al buscar el usuario por el Documento");
                }
            })
            .then(usuario => {
                if (usuario.hasOwnProperty('Usu_Documento')) {
                    const tablaBody = document.getElementById("tabla1-body");
                    tablaBody.innerHTML = "";

                    const newRow = document.createElement("tr");
                    newRow.innerHTML = `
                    
                    
                        <td>${usuario.Usu_Documento}</td>
                        <td>${usuario.Usu_Nombre}</td>
                        <td>${usuario.Usu_Apellido}</td>
                        <td>${usuario.Usu_tipo}</td>
                        <td>${usuario.Usu_Celular}</td>
                        <td>${usuario.Usu_Correo}</td>
                        <td>${usuario.Usu_Ficha}</td>
                        <td>
                        </td>
                    `;

                    tablaBody.appendChild(newRow);
                } else {
                    Swal.fire({
                        title: "Elemento No Encontrado",
                        icon: "error", 
                        confirmButtonText: "Aceptar"
                    })
                    Consultar();
                }
            })
            .catch(error => {
                console.error("Error al buscar el usuario por ID:", error);
                alert("Error al buscar el usuario por ID");
            });
        } else {
            console.error("Debe ingresar un ID de usuario válido");
        }
    });
});



//funciones adicionale

function mostrarCantidadUsuarios(){
    fetch("http://127.0.0.1:8000/ContarUsuarios", {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        const cantidad = document.querySelector('.cantidad');

        
        // Actualizar los contadores con los datos obtenidos
        cantidad.textContent = `Total de usuarios : ${data.cantidad_usuarios}`;

    })
    .catch(error => {
        console.error("Error al obtener la cantidad de usuarios:", error);
    });
}


document.addEventListener("DOMContentLoaded", function () {
    mostrarCantidadUsuarios();
});


