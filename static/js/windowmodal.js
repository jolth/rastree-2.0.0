(function($){

    // $('.modal_window').jtModal
    $.fn.jtModal = function() {
        // Si la carga es muy alta poner esta clase directamente en la ventana modal
        $(this).addClass('modalwindow'); 
        //
        // Obtener la altura y la anchura de la página
        var window_width = $(window).width();
        var window_height = $(window).height();
        //
        // Obtener la altura y la anchura del modal
        var modal_height = $(this).outerHeight();
        var modal_width = $(this).outerWidth();
        //
        // Calcular la parte superior y desplazada a la izquierda 
        // lo necesaria para el centrado
        var top = (window_height-modal_height)/2;
        var left = (window_width-modal_width)/2; 
        //
        // Aplicar nuevos valores CSS superior e izquierdo
        //$(this).css({'top' : top , 'left' : left, 'width': window_width, 'height':window_height});
        $(this).css({'top' : top , 'left' : left});
        /*return this.each(function(){
                // realizar algo
        });*/
    };
})(jQuery);

/* LAS FUNCIONES */
           
function close_modal(){
    // ocultar la mÃ¡scara
    $('#mask').fadeOut(500);
    // ocultar ventana modal(s)
    $('.modalwindow').fadeOut(500);
}

function show_modal(modal_id){
    // pone display a block y opacity a 0 para que podamos usar fadeTo
    $('#mask').css({ 'display' : 'block', opacity : 0});
    // se desvandece la mask a opacity 0.8
    $('#mask').fadeTo(500,0.8);
    // mostrar la ventana modal
    $('#'+modal_id).fadeIn(500);

    $('#'+modal_id).css('display','block');
}
