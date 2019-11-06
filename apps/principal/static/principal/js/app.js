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


$(document).ready(function(){
    $("#registro").validate({
        errorClass: 'is-invalid',
        rules:{
            username:{
                required: true
            },
            password1: "required",
            password2: {
            required: true,
            equalTo: "#password1"
            },
            email:{
                required: true,
                email: true
            }
        },
        messages:{
            username:{
                required:"¡Yo esperaba una dirección de correo!"
            },
            password1: {
                required: 'Falta ingresar contraseña',
                minlength: 'Largo insuficiente'
              },
            password2: {
                required: 'Falta reingresar la contraseña',
                equalTo: 'Las contraseñas ingresadas no coinciden',
                minlength: 'Largo insuficiente'
        
            },
            email:{
                required:"¡Yo esperaba una dirección de correo!",
                email: "¡La dirección de correo no es válida!"
            },
           

        }
    })
})
$("#registro").submit(function(){
    if($("#registro").valid()){
        return true;
    }else{
        Swal.fire({
            type: 'error',
            title:'Oops',
            text: 'Te faltaron ingresar algunos datos',
            footer: '<a href>¿Tienes algun problema?</a>'
          })
    }
    return false
})