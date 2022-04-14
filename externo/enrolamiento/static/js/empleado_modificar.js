const csrftoken = Cookies.get("csrftoken");
let datosEmpleados = null;

const getEmpleado = function () {
    let link = window.location.pathname;
    link = link.substring(0,link.length - 1);
    console.log(link)
    let id = link.replace('/empleado/modificar/', '');
    console.log("ID: ", id)
    let url = `http://localhost:8000/api/empleado/modificar/${id}/`;
    fetch(url, {
        method: 'PATCH', // or 'PUT'
        headers:{
            "X-CSRFToken": csrftoken,
        }
        }).then(response => response.json())
        .then(data => 
            actualizarCampos(data))
        console.log("Datos fetch: ")
        
        //  
            }

    const actualizarCampos = (data) => {
        $("#inputNombre").val(data.nombre) ;
        $("#inputRut").val(data.rut);
        $("#inputTelefono").val(data.telefono);
        console.log("DATA FOTO: ")
        console.log(data.foto);
        $("#fotoDisplay").attr("src",`http://localhost:8000${data.foto}`);
        
       };

    const putEmpleado = function () {
        let link = window.location.pathname;
        link = link.substring(0,link.length - 1);
        console.log(link)
        let id = link.replace('/empleado/modificar/', '');
        console.log("ID: ", id)
        let url = `http://localhost:8000/api/empleado/modificar/${id}/`;
        fetch(url, {
            method: 'PUT', // or 'PUT',
            body: JSON.stringify({
                nombre: $("#inputNombre").val(),
                rut: $("#inputRut").val(),
                telefono: $("#inputTelefono").val(),
                foto: null,
        }),
            headers:{"content-type": "application/json",
                "X-CSRFToken": csrftoken,
            }
            }).then(response => response.json())
            .then(data => 
                console.log(data))
            console.log("Datos fetch: ")
            
            //  
                }    

    const formu = document.getElementById("formModificarEmpleado");
    formu.addEventListener("submit", function(event){
        event.preventDefault();
        console.log(event);
        console.log("Evento submit  detectado")
    })

$(document).ready( function () {
    console.log("Inicio");
    getEmpleado();
  });

