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

// INSERTAR EQUIPO


