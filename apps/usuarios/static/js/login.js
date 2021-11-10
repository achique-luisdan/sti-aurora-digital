var estaIngresandoElNombreDeUsuario = true;
var esValidoElUsuario = false;
var textoDelBoton = {
    continuar: 'Continuar',
    iniciar: 'Iniciar'
};
var patternCamposVacios = /^\s*$/
setEstadoDeElementos();

var user = {
    username: '',
    firstName: '',
    lastName: '',
    password: '',
    foto: 'foto.jpg',
    fullName: function() {
        return this.firstName +' '+this.lastName;
    }
};


$('#iniciar-sesion').click(function(e) {
    e.preventDefault();

    if (estaVacio($('#nombre-login').val())) {
        alertify.alert('Hey!','(*) Por favor ingrese el nombre de su usuario');
    } else {

        if (estaIngresandoElNombreDeUsuario) {
            verificar_usuario();
            
        } else {
            validarClave();
        }
    }

});


function estaVacio(campo) {
    return patternCamposVacios.test(campo);
}

function verificar_usuario() {
    $.ajax({
            url: '/usuarios/'+$('#nombre-login').val().trim(),
            dataType: 'json',
            type: 'GET'
        })
        .done(function(response, status) {   
                setDatosDelUsuario(response);
                cambiarEstadoDeElementos();
                console.log(response);
        })
         .fail(function(e) {
            alertify.alert('Hey!', '(*) Usuario incorrecto!');
            console.log(e);
        });
}

function setEstadoDeElementos() {
    $('#iniciar-sesion').text(textoDelBoton.continuar);
    $('#grupo-clave').hide();
}

function setDatosDelUsuario(usuario) {
    user.firstName = usuario.firstName;
    user.lastName = usuario.lastName;
    user.password = usuario.password;

    $('#foto-login').attr('src', user.foto);
    $('#fullName').text(user.fullName());
}

function cambiarEstadoDeElementos() {
    estaIngresandoElNombreDeUsuario = false;
    esValidoElUsuario = true;
    $('#iniciar-sesion').text(textoDelBoton.iniciar);
    $('#grupo-clave').show();
    $('#grupo-nombre').hide();
}

function validarClave() {
    if (estaVacio($('#clave-login').val())) {
        alertify.alert('Hey!', '(*) Por favor ingresa la contraseña!');
    } else {
        if ($('#clave-login').val() != user.password) {
            alertify.alert('Hey!','(*) La clave es incorrecta.');
        } else {
            iniciarSesion();
        }
    }

}

function iniciarSesion() {
    alertify.alert('Hola, '+user.fullName()+' !', 'Bienvenido a tu casa de aprendizaje. ');
}
