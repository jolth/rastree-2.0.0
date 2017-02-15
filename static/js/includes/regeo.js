/* 
 * Autor: Jorge Alonso Toro 
 * Correo: jolthgs@gmail.com 
 * Fecha: ene 26 11:56:52 COT 2013 
 *
 * reverse geocoding
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
                    element.innerText = results[0].formatted_address;
                } else {
                    //$(element).text('NULL');
                    element.innerText = results[0].formatted_address;
                }
            } else {
                //$(element).text('false');
                element.innerText = results[0].formatted_address;
            }
    }); 
}
