console.log("Pruebaa")
const csrftoken = Cookies.get("csrftoken");
function encodeImageFileAsURL(element) {
    let file = element.files[0];
    let reader = new FileReader();
    reader.onloadend = function() {
      console.log('RESULT', reader.result)
    }
    reader.readAsDataURL(file);

    return reader.result
  }

// Porcentaje Total 
const enrolamiento = function () {
    let encode = "";
    let foto = document.getElementById("imagen");
    //encode = encodeImageFileAsURL(foto);
    let dispositivo = 1
    let usuario = 1
    let ingreso = "2022-04-27 23:03:00-04"
    let salida = "2022-04-28 21:03:00-05"
    var url = 'http://127.0.0.1:8000/api/ingreso/crear';

    const formData = new FormData();

    const file = $("#imagen")[0].files[0];
    documento = $("#imagen")[0].files[0],file.fileName;
        formData.append('imagen', file);
        formData.append('empleado', usuario);
        formData.append('dispositivo', dispositivo);
        formData.append('ingreso', ingreso);
        formData.append('salida', salida);

        console.log("AAAAAAAAAA DOCUMENTO");
        console.log($("#imagen")[0].files[0],file.fileName);

fetch(url, {
  method: 'POST', // or 'PUT'
  body: formData,// data can be `string` or {object}!
  headers:{
    "X-CSRFToken": csrftoken,
  }
}).then(res => res.json())
.catch(error => console.error('Error:', error))
.then(response => console.log('Success:', response));

    }
    

    let btn = document.getElementById("enviarImagen");
btn.addEventListener('click', event => {
    enrolamiento();
});