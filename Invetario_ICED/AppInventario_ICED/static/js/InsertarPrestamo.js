
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormPrestamos").addEventListener("submit",function(event) {
        event.preventDefault();
        
        var Datos={
            Pres_Id:document.getElementById("Pres_Id").value,
            Pres_Equipos_id_id:document.getElementById("Pres_Equipos_id_id").value,
            Pres_Usuarios_Documento_id:document.getElementById("Pres_Usuarios_Documento_id").value,
            Pres_Fec_Entrega:document.getElementById("Pres_Fec_Entrega").value,
            Pres_Fec_Devolucion:document.getElementById("Pres_Fec_Devolucion").value,
            Pres_Hora_Entrega:document.getElementById("Pres_Hora_Entrega").value,
            Pres_Hora_Devolucion:document.getElementById("Pres_Hora_Devolucion").value,
            Pres_Tiempo_Limite:document.getElementById("Pres_Tiempo_Limite").value,
            Pres_Observaciones_entrega:document.getElementById("Pres_Observaciones_entrega").value,
            Pres_Observaciones_recibido:document.getElementById("Pres_Observaciones_recibido").value,
        };

        var data = {
            'Pres_Id': Pres_Id,
            'Pres_Equipos_id_id': Pres_Equipos_id,
            'Pres_Usuarios_Documento_id': Pres_Usuarios_Documento_id,
            'Pres_Fec_Entrega': Pres_Fec_Entrega,
            'Pres_Fec_Devolucion': Pres_Fec_Devolucion,
            'Pres_Hora_Entrega': Pres_Hora_Entrega,
            'Pres_Hora_Devolucion': Pres_Hora_Devolucion,
            'Pres_Tiempo_Limite': Pres_Tiempo_Limite,
            'Pres_Observaciones_entrega': Pres_Observaciones_entrega,
            'Pres_Observaciones_recibido': Pres_Observaciones_recibido
        };

        console.log(document.getElementById("Pres_Id").value)
        
        var JsonData=JSON.stringify(Datos);
        console.log(JsonData)
        fetch("http://127.0.0.1:8000/insertarPrestamo/",{
            method:"POST",
            body: JSON.stringify(data),
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
        console.error("Error al guardar los datos:", error);

        
    })

})

