console.log("Pruebaa")

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
    foto = document.getElementById("imagen");
    enconde = encodeImageFileAsURL(foto);
    fetch(
  
        `http://127.0.0.1:8000/`,
        {
            method: "POST",
            body: JSON.stringify({
                enconde,
                
            }),
            headers: {
                "content-type": "application/json",
                
                "X-CSRFToken": csrftoken,
            },
        }
    ).then(async (response) => {
        const textoRespuesta = await response.json();
        if (response.status === 400) {
            if (textoRespuesta.codigo[0].includes("enrolamiento")) {
                
                Swal.fire(
                    "Cancelado",
                    "Error",
                    "error"
                );
            } else {
              
                toastr.error(
                    "Ha ocurrido un inconveniente, intente más tarde"
                );
            }
        } else if (response.ok) {
            console.log("Enrolamiento Exitoso")
        } else {
            toastr.error(
                "Ha ocurrido un inconveniente, intente más tarde"
            );
        }
    });
    }