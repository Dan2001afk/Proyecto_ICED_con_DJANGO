//AGREGAR EQUIPO
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormEquipos").addEventListener("submit",function(event) {
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
        fetch("http://127.0.0.1:8000/insertar/",{
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

