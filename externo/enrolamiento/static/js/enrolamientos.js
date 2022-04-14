const csrftoken = Cookies.get("csrftoken");

const getEnrolamientos = function () {
    let url = 'http://127.0.0.1:8000/api/ingresos/';
    fetch(url, {
        method: 'GET', // or 'PUT'
        headers:{"content-type": "application/json",
            "X-CSRFToken": csrftoken,
        }
        }).then(response => response.json())
        .then(data => 
        listadoEnrolamientos(data))
        console.log("Datos fetch: ")

        //
            }

    const listadoEnrolamientos = (data) => {
    
        console.log("Datos: ")
        console.log(data);
        
        
        document.getElementById("tablaEnrolamientos").innerHTML +=
        `
        
        <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Empleado</th>
              <th scope="col">Dispositivo</th>
              <th scope="col">Ingreso</th>
              <th scope="col">Salida</th>
              <th scope="col">Foto</th>
            </tr>
          </thead>

`

        let bloque = data.forEach(function (element, indice, array) {
            console.log(indice);
            $("#tablaEnrolamientos").append(
                `<tr>
                <th scope="row">${element.id}</th>
                <td>
                <a href="http://localhost:8001/empleado/modificar/1/">${element.empleado}</a>
                </td>
                <td>${element.dispositivo}</td>
                <td>${element.ingreso}</td>
                <td>${element.salida}</td>
                <td> <img src="${element.foto}" width="100" height="100"> </td>
              </tr>`
            );

        })};


$(document).ready( function () {
    console.log("Inicio");
    getEnrolamientos();
  });

