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
                        <td>${dato.Documento_Usuario}</td> <!-- Agrega el campo del documento del usuario -->
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