// Contenido de Crud-VistasUsuarios.js

// Lógica para cargar y mostrar los datos JSON en la tabla
async function cargarDatos() {
    try {
        const response = await fetch('/listar_datos/'); // Cambia la URL a la ruta correcta
        const datos = await response.json();
        const tablaBody = document.getElementById('tabla1-body');

        if (datos.length === 0) {
            tablaBody.innerHTML = '<tr><td colspan="7">No hay datos disponibles</td></tr>';
        } else {
            tablaBody.innerHTML = '';
            datos.forEach(dato => {
                const fila = `
                    <tr>
                        <td>${dato.Dispositivo}</td>
                        <td>${dato.Observaciones}</td>
                        <td>${dato.Serial}</td>
                        <td>${dato.Especialidad}</td>
                        <td>${dato.Pres_Hora_Entrega}</td>
                    </tr>
                `;
                tablaBody.innerHTML += fila;
            });
        }
    } catch (error) {
        console.error('Error al cargar los datos:', error);
    }
}

// Llama a la función para cargar los datos cuando se cargue la página
window.onload = cargarDatos;


/*CONTADOR CANTIDAD DE EQUIPOS*/

function equiposActivos() {
    fetch("http://127.0.0.1:8000/ContarActivos", {
        method: "GET",
        headers: {
            "consultar-Type": "AppInventario_ICED/json"
        }
    })
    .then(response => response.json())
    .then(data => {

        const activos = document.querySelector('.activos');

        
        // Actualizar los contadores con los datos obtenidos
        activos.textContent = `Total de equipos activos: ${data.cantidad_equipos_activos}`;

    })
    .catch(error => {
        console.error("Error al obtener la cantidad de equipos activos:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
    equiposActivos();
});


