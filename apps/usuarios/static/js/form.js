function validarInputs() {
    var centinela = false;
    if (validarTextVacios() && coincidenciaContrasea() && validarSeleccionRadio() && validarSeleccionCheckBox()){
        centinela = true;
    }    
    return centinela;
}

function validarTextVacios(){
    var formulario = document.formulario_registro,
    elementos = formulario.elements;
    var bandera = true;    
    for (var i = 0; i < elementos.length; i++) {
        if (elementos[i].type == "text" || elementos[i].type == "email" || elementos[i].type == "password") {
            if (elementos[i].value.length == 0) {                
                /*alertify.error('Error notification message.');*/ 
                elementos[i].className = elementos[i].className + " error";
                alertify.alert('(*) '+ elementos[i].name +' [Campo Obligatorio]', 'El campo ' + elementos[i].name + ' esta incompleto');
                bandera = false;
                return bandera;
            } 
            else {
                elementos[i].className = elementos[i].className.replace(" error", "");
                bandera = true;
            }
        }
    }
    return bandera;
}

function validarSeleccionRadio(){
    var formulario = document.formulario_registro,
    elementos = formulario.elements;
    var centinela = false;
    var bandera = true; 
    var opciones = document.getElementsByName('sexo');   
    for (var i = 0; i < elementos.length; i++) {
        if(elementos[i].type == "radio" && elementos[i].name == 'sexo'){
            for (var o = 0; o < opciones.length; o++) {
                if (opciones[o].checked) {
                    centinela = true;
                }
                if (centinela == false) {
                    elementos[i].parentNode.className = elementos[i].parentNode.className + " error";
                    centinela = false;
                } 
                else {
                    elementos[i].parentNode.className = elementos[i].parentNode.className.replace(" error", "");
                    centinela = true;
                }
            }
        }
    }
    return centinela;
}


function validarSeleccionCheckBox(){
    var opcion = document.getElementsByName('terminos');
    var resultado = false;
    var formulario = document.formulario_registro,
    elementos = formulario.elements;   
    for (var i = 0; i < elementos.length; i++) {
        if(elementos[i].type == "checkbox"){
            for (var o = 0; o < opcion.length; o++) {
                if (opcion[o].checked) {
                    resultado = true;
                    break;
                }
            }
            if (resultado == false) {
                elementos[i].parentNode.className = elementos[i].parentNode.className + " error";
            } 
            else {
                elementos[i].parentNode.className = elementos[i].parentNode.className.replace(" error", "");
            }
        }
    }
    return resultado;
}

function coincidenciaContrasea(){
   var formulario = document.formulario_registro,
    elementos = formulario.elements;
    if (elementos.password1.value !== elementos.password2.value) {
        elementos.password1.value = "";
        elementos.password2.value = "";
        elementos.password1.className = elementos.password1.className + " error";
        elementos.password2.className = elementos.password2.className + " error";
        alert("Las contraseñas no coinciden.")
        return false;
    } 
    else {
        elementos.password1.className = elementos.password1.className.replace(" error", "");
        elementos.password2.className = elementos.password2.className.replace(" error", "");
        return true;
    }
}

(function(){
    var formulario = document.formulario_registro,
    elementos = formulario.elements;
    var focusInput = function(){
        this.parentElement.children[1].className = "label active";
        this.parentElement.children[0].className = this.parentElement.children[0].className.replace("error", "");
    };

    var blurInput = function(){
        if (this.value <= 0) {
            this.parentElement.children[1].className = "label";
            this.parentElement.children[0].className = this.parentElement.children[0].className + " error";
        }
    };

    for (var i = 0; i < elementos.length; i++) {
        if (elementos[i].type == "text" || elementos[i].type == "email" || elementos[i].type == "password") {
            elementos[i].addEventListener("focus", focusInput);
            elementos[i].addEventListener("blur", blurInput);
        }
    }    
}())


function validarSeleccionAspiracion(){
    var formulario = document.formulario_registro,
    elementos = formulario.elements;
    var centinela = false;
    var bandera = true; 
    var opciones = document.getElementsByName('aspiraciones');   
    for (var i = 0; i < elementos.length; i++) {
        if(elementos[i].type == "radio" && elementos[i].name == 'aspiraciones'){
            for (var o = 0; o < opciones.length; o++) {
                if (opciones[o].checked) {
                    centinela = true;
                }
                if (centinela == false) {
                    elementos[i].parentNode.className = elementos[i].parentNode.className + " error";
                    centinela = false;
                } 
                else {
                    elementos[i].parentNode.className = elementos[i].parentNode.className.replace(" error", "");
                    centinela = true;
                }
            }
        }
    }
    if(centinela == false){
       alertify.alert('(*) Aspiración[Campo obligatorio]', 'Por favor. Seleccione la aspiración de su preferencia.');
    }
    return centinela;
}