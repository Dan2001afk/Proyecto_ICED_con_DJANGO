//AGREGAR USUARIO
document.addEventListener("DOMContentLoaded",function(){
    document.getElementById("FormUsuarios").addEventListener("submit",function(event) {
        event.preventDefault();
        
        var Datos={
            Usu_Documento:document.getElementById("Usu_Documento").value,
            Usu_Nombre:document.getElementById("Usu_Nombre").value,
            Usu_Apellido:document.getElementById("Usu_Apellido").value,
            Usu_tipo:document.getElementById("Usu_tipo").value,
            Usu_Celular:document.getElementById("Usu_Celular").value,
            Usu_Correo:document.getElementById("Usu_Correo").value,
            Usu_Ficha:document.getElementById("Usu_Ficha").value
        };
        console.log(document.getElementById("Usu_Documento").value)

        var JsonData=JSON.stringify(Datos);
        console.log(JsonData)
        fetch("http://127.0.0.1:8000/insertarUsuario/",{
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

