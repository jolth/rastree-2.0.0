/*
 * Autor: Jorge A. Toro
 * */

var regeocoding = function(lat, lng, element) {
    /* función que resive la latitud y logitud y retorna su
     * codigicación inversa */
    var geocoder = new google.maps.Geocoder(); 

    var latlng = new google.maps.LatLng(lat, lng);

    geocoder.geocode({'latLng': latlng}, function(results, status){
            if (status == google.maps.GeocoderStatus.OK) {
                if (results[0]) {
                    //$(element).text(results[1].formatted_address);
                    //element.innerText = results[0].formatted_address;
                    $(element).attr('data-content', results[0].formatted_address);
                } else {
                    //$(element).text('NULL');
                    //element.innerText = results[0].formatted_address;
                    $(element).attr('data-content', 'Colombia');
                }
            } else {
                //$(element).text('false');
                //element.innerText = results[0].formatted_address;
                $(element).attr('data-content', 'Colombia');
            }
    }); 
}


$('.sl_name').each(function(id, e) {
    if (!($(e).attr('data-content'))) {
        var lat, lng, position;
        position = $(e).attr('data-position');
        position = position.split(',', 2);
        lat = parseFloat(position[0]); 
        lng = parseFloat(position[1]); 
        //console.log("LAT: "+ lat);
        //console.log("LNG: "+ lng);
        regeocoding(lat, lng, e);
    } 
});

