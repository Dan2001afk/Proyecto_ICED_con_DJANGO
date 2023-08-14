//Listar Prestamos
function Listar(){
    fetch("http://127.0.0.1:8000/ListarPrestamos",{
        method:"GET",
        Headers:{
            "consultar-Type":"AppInventario_ICED/json"
        }
    })
    .then(Response => Response.json())
    .then(datos=>{
        console.log(datos)
        let tabla=document.querySelector('#tabla1-body');
        tabla.innerHTML="";
        if (datos==0) {
            tabla.innerHTML+=`<tr> <td> no hay datos </td> </tr>`
        }
        else{
            for (let dat of datos) {
                tabla.innerHTML+=`
                <tr>
                <td>${dat.Pres_Id}</td>
                <td>${dat.Pres_Equipos_id}</td>
                <td>${dat.Pres_Usuarios_Documento_id}</td>
                <td>${dat.Pres_Fec_Entrega}</td>
                <td>${dat.Pres_Hora_Entrega}</td>
                <td>${dat.Pres_Tiempo_Limite}</td>
                <td>${dat.Pres_Observaciones_entrega}</td>
                </tr>`
            }
        }
    });
}

//Agregar un Prestamo
function Agregar(){
    document.addEventListener("DOMContentLoaded",function(){
        document.getElementById("FormPrestamos").addEventListener("submit",function(event) {
            event.preventDefault();
            
            var Datos={
                Pres_Id:document.getElementById("Pres_Id").value,
                Pres_Equipos_id:document.getElementById("Pres_Equipos_id").value,
                Pres_Usuarios_Documento_id:document.getElementById("Pres_Usuarios_Documento_id").value,
                Pres_Fec_Entrega:document.getElementById("Pres_Fec_Entrega").value,
                Pres_Hora_Entrega:document.getElementById("Pres_Hora_Entrega").value,
                Pres_Tiempo_Limite:document.getElementById("Pres_Tiempo_Limite").value,
                Pres_Observaciones_entrega:document.getElementById("Pres_Observaciones_entrega").value
            };
            console.log(document.getElementById("Pres_Id").value)
    
            var JsonData=JSON.stringify(Datos);
            console.log(JsonData)
            fetch("http://127.0.0.1:8000/insertarPrestamo/",{
                method:"POST",
                body: JsonData,
                headers:{
                    "Content-Type":"AppInventario_ICED/json"
                }
            
            })
    
            .then(response => response.json())
            .then(datoos=>{
                console.log(datoos)
                ConsultarPrestamos();
            })
    
            .catch(console.error()) 
    
            
        });
    
    });
}

