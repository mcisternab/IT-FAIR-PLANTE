$(document).ready(function(){
    $("#login").validate({
        errorClass: 'is-invalid',
        rules:{
            username:{
                required:true
            },
            password:{
                required:true
            }
           
        },
        messages:{
            username:{
                required:"Se debe ingresar el nombre"
            },
            password:{
                required:"¡Yo esperaba una dirección de correo!"
            }
           

        }
    })
})
$("#login").submit(function(){
    if($("#login").valid()){
        return true;
    }else{
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'Te faltaron ingresar algunos datos!',
            footer: '<a href>Tienes algun problema?</a>'
          })
    }
    return false
})
