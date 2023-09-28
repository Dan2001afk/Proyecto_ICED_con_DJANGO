//ACTUALIZAR EQUIPO
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("ActualizarEquipos").addEventListener("submit",function(event) {
        event.preventDefault();
        var Datos={
            Equ_id:document.getElementById("Equ_id").value,
            Equi_tipo:document.getElementById("Equi_tipo").value,
            Equi_modelo:document.getElementById("Equi_modelo").value,
            Equi_color:document.getElementById("Equi_color").value,
            Equi_serial:document.getElementById("Equi_serial").value,
            Equi_estado:document.getElementById("Equi_estado").value,
            equi_especialidad:document.getElementById("equi_especialidad").value
        };
        console.log(document.getElementById("Equ_id").value)

        var JsonData=JSON.stringify(Datos);
        console.log(JsonData)
        fetch("http://127.0.0.1:8000/ActualizarEquipo",{
            method:"POST",
            body:JsonData,
            headers:{
                "Content-Type":"AppInventario_ICED/json"
            }

        })

        .then(response => response.json())
        .then(datoos=>{
            console.log(datoos)
            Consultar();
        })

        .catch(console.error())


        
    })

})

//AGREGAR EQUIPO
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("FormEquipos").addEventListener("submit", function (event) {
        event.preventDefault();

        var Datos = {
            Equi_tipo: document.getElementById("Equi_tipo").value,
            Equi_modelo: document.getElementById("Equi_modelo").value,
            Equi_color: document.getElementById("Equi_color").value,
            Equi_serial: document.getElementById("Equi_serial").value,
            Equi_estado: document.getElementById("Equi_estado").value,
            equi_especialidad: document.getElementById("equi_especialidad").value
        };

        var JsonData = JSON.stringify(Datos);
        console.log(JsonData);

        fetch("http://127.0.0.1:8000/insertar/", {
            method: "POST",
            body: JsonData,
            headers: {
                "Content-Type": "application/json" // Fixed the Content-Type header value
            }
        })
        .then(response => response.json())
        .then(datoos => {
            console.log(datoos);
            Consultar();
            alert("Datos enviados exitosamente."); // Alert when data is sent
        })
        .catch(error => {
            console.error(error);
            alert("Error al enviar los datos."); // Alert for error
        });
    });
});



//Eliminar Equipo
function eliminarEquipo(prestamoId) {
    const url = `http://127.0.0.1:8000/EliminarPrestamo/${prestamoId}`;

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
                Listar(); 
                mostrarCantidadPrestamos();
                Swal.fire("Éxito", "Registro eliminado exitosamente.", "success");
            })
            .catch(error => {
                console.error("Error al eliminar el equipo:", error);
                Swal.fire("Error", "Error al eliminar el equipo.", "error");
            });
        }
    });
}


