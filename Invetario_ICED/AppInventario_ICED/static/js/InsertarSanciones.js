//Agregar Sanciones
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormSanciones").addEventListener("submit",function(event) {
        event.preventDefault();
        
        var Datos={
            San_Pres_id:document.getElementById("San_Pres_id").value,
            San_Fecha:document.getElementById("San_Fecha").value,
            San_Hora:document.getElementById("San_Hora").value,
            San_tiempo:document.getElementById("San_tiempo").value,
            San_Descripcion:document.getElementById("San_Descripcion").value
        };
        console.log(document.getElementById("San_Pres_id").value)
        console.log(Datos)

        var JsonData=JSON.stringify(Datos);
        console.log(JsonData)
        fetch("http://127.0.0.1:8000/insertarSancion/",{
            method:"POST",
            body:JsonData,
            headers:{
                "Content-Type":"AppInventario_ICED/json"
            }
        })
        .then(response => response.json())
        .then(datoos=>{
            console.log(datoos)
            ConsultarSanciones();
        })
        .catch(console.error())
    })

})



