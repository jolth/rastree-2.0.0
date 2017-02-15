/* [ ---- Action Common ---- ] */

$(document).ready(function(){
    //* pone class="active" en el link 
    link_active.init();
});

//* Pone class="active" en el link que 
// contenga la URL actual.
link_active = {
    init: function (){
        var path = document.location.pathname;

        $('nav a').each(function(){ 
                 var href = $(this).attr('href');
                 console.log(href + '==' + path);
                 if (path == href){
                    $(this).parent().addClass('active');
                    console.log($(this).parent().addClass('active'));
                 } else {
                    $(this).parent().removeClass('active');
                 }
         });
    }
};
