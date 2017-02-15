/* [ ---- Gebo Action Common ---- ] */

$(document).ready(function(){

    //* Sidebar info Common  
    gebo_sidebar_info_common.init();
    //* pone class="active" en el link 
    gebo_link_active.init();
});

//* Sidebar info Common
gebo_sidebar_info_common = {
    init: function() {
        var s_box = $('.sidebar_info');
        gebo_sidebar_info_common.vehi_on(s_box);
        gebo_sidebar_info_common.vehi_off(s_box);
        gebo_sidebar_info_common.vehi_alert(s_box);
    },
    vehi_on: function (s_box){
        s_box.find('.act-success').text('30')
    },
    vehi_off: function (s_box) {
        s_box.find('.act-danger').text('30')
    },
    vehi_alert: function (s_box){
        s_box.find('.act-warning').text('30')
    }
};

//* Pone class="active" en el link que 
// contenga la URL actual.
gebo_link_active = {
    init: function (){
        var path = document.location.pathname;

        $('nav a').each(function(){ 
                 var href = $(this).attr('href');
                 //console.log(href + '==' + path);
                 if (path == href){
                    $(this).parent().addClass('active');
                    //console.log($(this).parent().addClass('active'));
                 } else {
                    $(this).parent().removeClass('active');
                 }
         });
    }
};
