var current_fs, next_fs, previous_fs; //fieldsets
var left, opacity, scale; //fieldset properties which we will animate
var animating; //flag to prevent quick multi-click glitches

$(document).ready(function(){  
    $('.datepicker').datepicker({
        format: 'dd/mm/yyyy',
    });
});

$(".next").click(function(){
    var centinela = false;
    if ($(this).parent().index() == 1){
        if(validarInputs()){
            centinela = true;
        }
    }
    else if ($(this).parent().index() == 2) {
         if(validarSeleccionAspiracion()){
            centinela = true;  
         }             
    }

    if(centinela){
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();
        //activate next step on progressbar using the index of next_fs
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        next_fs.show();
        current_fs.hide();
    }
});














/*
$(".previous").click(function(){
	if(animating) return false;
	animating = true;
	
	current_fs = $(this).parent();
	previous_fs = $(this).parent().prev();
	
	
	//de-activate current step on progressbar
	$("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
	
	//show the previous fieldset
	current_fs.hide();
	previous_fs.show(); 
});

$(".submit").click(function(){
	return false;
})*/