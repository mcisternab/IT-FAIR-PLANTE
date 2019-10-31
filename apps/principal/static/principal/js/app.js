$(document).ready(function(){
    $("#registro").validate({
        errorClass: 'is-invalid',
        rules:{
            username:{
                required:true
            },
            apellido:{
                required:true
            },
            password: "required",
            password2: {
            required: true,
            equalTo: "#password"
            },
            correo:{
                required:true,
                email:true
            },
            fnacimiento:{
                required:true
            },
            Comuna:{
                required:true
            },
            ncontacto:{
                required:true
            }
           
        },
        messages:{
            username:{
                required:"Se debe ingresar el nombre de usuario"
            },
            apellido:{
                required:"Se debe ingresar el apellido"
            },
            password: {
                required: 'Falta ingresar contraseña',
                minlength: 'Largo insuficiente'
              },
              password2: {
                required: 'Falta reingresar la contraseña',
                equalTo: 'Las contraseñas ingresadas no coinciden',
                minlength: 'Largo insuficiente'
        
            },
            correo:{
                required:"¡Yo esperaba una dirección de correo!",
                email: "¡La dirección de correo no es válida!"
            },
            fnacimiento:{
                required: "Se debe ingresar fecha de nacimiento"
            },
            cperros:{
                required: "Se debe ingresar cantidad de perros"
            },
            Comuna:{
                required: "Le falta ingresar la comuna"
            },
            ncontacto:{
                required: "Le falta ingresar número de contacto"
            }
           

        }
    })
})
$("#registro").submit(function(){
    if($("#registro").valid()){
        return true;
    }else{
        Swal.fire({
            type: 'error',
            title: 'Oops...',
            text: 'Te faltaron ingresar algunos datos!',
            footer: '<a href>¿Tienes algun problema?</a>'
          })
    }
    return false
})


$(document).ready(function(){
    $("#Inicio").validate({
        errorClass: 'is-invalid',
        rules:{
            username:{
                required: true,
                email: true
            },
            contraseña:{
                required:true
            }
        },
        messages:{
            username:{
                required:"¡Yo esperaba una dirección de correo!",
                email: "¡La dirección de correo no es válida!"
            },
            contraseña:{
                required:"Debe ingresar su contraseña"
            }
           

        }
    })
})
$("#Inicio").submit(function(){
    if($("#Inicio").valid()){
        return true;
    }else{
        Swal.fire({
            type: 'error',
            title:'Los datos son incorrectos',
            text: 'Por favor, ingresa correctamente los datos ',
            footer: '<a href>¿Haz olvidado tu contraseña?</a>'
          })
    }
    return false
})