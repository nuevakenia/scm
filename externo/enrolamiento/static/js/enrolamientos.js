

const getEnrolamientos = function () {
    let url = 'http://127.0.0.1:8000/api/ingresos/';
    fetch(url, {
        method: 'GET', // or 'PUT'
        headers:{"content-type": "application/json",
            "X-CSRFToken": csrftoken,
        }
        }).then(response => response.json())
        .then(data => console.log(data));
        console.log("aaaa")
        listadoEnrolamientos(data);
            }

    const listadoEnrolamientos = (data) => {
        console.log("Datos: ")
        console.log(data);
    
    
        let bloque = data.forEach(function (element, indice, array) {
            console.log(indice);
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
                <tbody>
                  <tr>
                    <th scope="row"></th>
                    <td>Mark</td>
                    <td>Otto</td>
                    <td>@mdo</td>
                  </tr>
                  <tr>
                    <th scope="row">2</th>
                    <td>Jacob</td>
                    <td>Thornton</td>
                    <td>@fat</td>
                  </tr>
                  <tr>
                    <th scope="row">3</th>
                    <td colspan="2">Larry the Bird</td>
                    <td>@twitter</td>
                  </tr>
                </tbody>
        
    `
        })};


$(document).ready( function () {
    console.log("xDDD");
    getEnrolamientos();
  });

  function yourfunction() { console.log("xDDD"); }

window.onload = yourfunction;