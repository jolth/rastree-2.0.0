/* [ ---- Action Common ---- ] */

$(document).ready(function(){
    //* pone class="active" en el link 
    link_active.init();
    // Gestión de Eventos
    getNumEvents();
    //setInterval(function(){getNumEvents();}, 60000);
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

//*
var getNumEvents = function(){ 
  var numevnt = null;
  $.getJSON('/user/listeventjson', function(data){
    //console.log(data); 
    numevnt = data[0].count; 
    //console.log(numevnt);
    //$('#badge0').text(numevnt)
    //            .addClass('badge');
    $('#badge1').text(numevnt);
  });
};

