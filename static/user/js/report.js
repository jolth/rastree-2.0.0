/* [ ---- Gebo Admin Panel - dashboard ---- ] */

// valor del href del botón de impresión
var href_btimp = document.getElementById('btimp').href;

$(document).ready(function() {
		//* table filter
		table_filter.init();
        
        //* resize map
        var mapHeight = jQuery('#row1').height();
        jQuery('#map_canvas').height(mapHeight-(mapHeight*11.50/100));
        // google-chrome
        jQuery(document).load(function(){
            var mapHeight = jQuery(this).height();
            jQuery('#map_canvas').height(mapHeight-(mapHeight*11.50/100));
        });
        //
        jQuery(window).resize(function(){
            var mapHeight = jQuery(this).height();
            jQuery('#map_canvas').height(mapHeight-(mapHeight*11.50/100));
        });

        //* popovers
        //jQuery('.icon-info-sign').popover('toggle');
        //jQuery('.icon-info-sign').popover('show');
        //jQuery('.icon-info-sign').popover('hide');
        jQuery('.icon-info-sign').hover(function (){ 
                $(this).popover('show');
        });

		//* resize elements on window resize
		/*var lastWindowHeight = $(window).height();
		var lastWindowWidth = $(window).width();
		$(window).on("debouncedresize",function() {
			if($(window).height()!=lastWindowHeight || $(window).width()!=lastWindowWidth){
				lastWindowHeight = $(window).height();
				lastWindowWidth = $(window).width();
				//* rebuild calendar
				//$('#calendar').fullCalendar('render');
			}
		});*/

        //* google map
        //map_dashboard.init();
        //map_dashboard.init(5.06798, -75.51738);
        map_dashboard.init(5.06798, -75.51738, 4);

        //* maps vehicles
        //maps_vehicle.init();

    //* datepicker
    var tdate = new Date();
    //var year  = tdate.getYear()+1900;
    var year  = tdate.getFullYear();
    var month = tdate.getMonth();
    var today = tdate.getDate();
    var hoy = new Date(year, month, today); 
    $('#dp5').datepicker({
            format: 'dd-mm-yyyy' 
            //format: 'yyyy-mm-dd' 
        })
        //.attr('value', today+'-'+month+'-'+year)
        //.attr('value', year+'-'+(month+1)+'-'+today)
        .attr('value', today+'-'+(month+1)+'-'+year)
        .on('changeDate', function(ev){
                    console.log("Datepicker:"+ev.date.valueOf()+': '+ev.date);
                    console.log("Hoy:"+hoy.valueOf()+': '+hoy);
                    if(ev.date.valueOf() > hoy.valueOf()){
                        $('#alert').show().find('strong').text('La fecha no puede ser mayor que la fecha de hoy.');
                    } else {
                        $('#alert').hide();
                        var fecha = new Date(ev.date);
                        var d=fecha.getDate(), m=fecha.getMonth(), y=fecha.getFullYear(); 
                        console.log("Buscar fecha: "+fecha);
                        console.log("Buscar fecha: "+ y+','+(m+1)+','+d);
                        button_print.init(); // Pone la fecha que se cambia en el href del botón para imprimir
                    }
                });


        //**
        get_events.init($('#submit'));

});

	//* table filter
	//gebo_flist = {
	table_filter = {
		init: function(){
			//*typeahead
			var list_source = [];
			//$('.table tr').each(function(){
			$('table input:text').each(function(){
				//var search_name = $(this).find('.sl_name').text();
				//var search_name = $(this).find('.sl_name').attr('value');
				//var search_name = $(this).find('.sl_name').attr('value');
				var search_name = $(this).attr('value');
                console.log('search_name: ' + search_name);
				//var search_email = $(this).find('.sl_email').text();
				list_source.push(search_name);
			});
			$('.user-list-search').typeahead({source: list_source, items:5});

            $('.user-list-search').change(function(){
                        var vehiculo = $(this).attr('value');
                        //console.log('cambia: ' + vehiculo);
                        $('#'+vehiculo).removeClass('hide');
                        // asignamos class="data" 
                        $('#'+vehiculo).find('input:text').addClass('data');
                        $('#form').removeClass('hide');
                        //console.log('cambia fin: ' + vehiculo);
                        button_print.init(); // Pone la fecha que se cambia en el href del botón para imprimir
                    });
		}

        //* formulario
        /*$("form").submit(function(){
            //aqui podemos llamar alguna funcion por defecto o nada. 
            //El return false va igual
            //return false;
                return false;
        });*/

	};

    button_print = {
        init: function() {
            //var href = $('#btimp').attr('href');
            var href = href_btimp;
            console.log("href: " + href);
            var fecha = $('.data-fecha').attr('value');
            var id = $('.data').attr('data-id'); 
            // ?carid=9&date=5-2-2013
            href = href + '?carid=' + id +'&'+ 'date=' + fecha;  
            $('#btimp').attr('href', href);
        } 
    };

//* google map 
map_dashboard = {
    init: function(lat, lng, zm){
        /*var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://maps.googleapis.com/maps/api/js?sensor=fale' 
        //script.src = 'https://maps.googleapis.com/maps/api/js?sensor=false&' +  
                     //'callback=map_dashboard.initialize(5.06798, -75.51738)';
        document.body.appendChild(script);*/
        google.maps.event.addDomListener(window, 'load', map_dashboard.initialize(lat, lng, zm));
    },
    initialize: function(lat, lng, zm){
        var mapOptions = {
            //zoom: 8,
            zoom: zm,
            //center: new google.maps.LatLng(5.06798,-75.51738),
            center: new google.maps.LatLng(lat, lng),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map_canvas'),
                                      mapOptions);
    },
    /*start: function(){
        google.maps.event.addDomListener(window, 'load', initialize);
    }*/
};

//* map vehicle 
map_vehicle = {
    init: function(lat, lng, zm, ubicacion){
            google.maps.event.addDomListener(window, 'load', map_vehicle.initialize(lat, lng, zm, ubicacion));
    },
    initialize: function(lat, lng, zm, ubicacion){
        var latlng = new google.maps.LatLng(lat,lng);
        var mapOptions = {
            zoom: zm,
             center: latlng,
            //center: new google.maps.LatLng(lat, lng),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map_canvas'),
                                      mapOptions);
        var image = '/static/img/trunkgreen.png';
        var marker = new google.maps.Marker({
          position: latlng,
          map: map,
          icon: image, 
          title: "Map"
        });

        var infowindow = new google.maps.InfoWindow(
            { //content: '<b>Posición:</b> ' + latlng + '<br>' + '<b>Ubicación:</b> ' + ubicacion,
              content: '<b>Ubicación:</b> ' + ubicacion,
              size: new google.maps.Size(50,50),
              position: latlng
        });
        google.maps.event.addListener(marker, 'click', function() {
            //map.setZoom(8);
            infowindow.open(map, marker);
        });
    },
    /*start: function(){
        google.maps.event.addDomListener(window, 'load', initialize);
    }*/
};

//* ubicación del vehículo en el mapa.
maps_vehicle = {
    init: function(){
        $('.ubica').on(
            'click',
            function(){
                //console.log('clic: ' + this);
                //console.log('position: ' + $(this).attr('data-position'));
                //map_vehicle.init($(this).attr('data-position'), 19);
                var position = $(this).attr('data-position').split(",");
                var ubicacion = $(this).attr('data-content')
                //console.log("POSITION: "+ position);
                //console.log("LAT: "+ position[0].substring(1));
                //console.log("LONG: "+ position[1].substring(0, position[1].length-1));
                var lat = position[0].substring(1);
                var lng = position[1].substring(0, position[1].length-1);
                //map_vehicle.init(position[0], position[1], 19, ubicacion);
                map_vehicle.init(lat, lng, 19, ubicacion);
                //console.log('position: ' + $(this).attr('data-position'));
                //console.log('[position]: ' + position[0]);
                //console.log(ubicacion);
            });
    }
};


//* Obtiene los eventos del vehiculo con JSON
get_events = {
    init: function(elem){
        
        $(elem).on('click', function(){
                // fecha:
                var fecha = $('.data-fecha').attr('value');
                // id del vehiculo:
                var vehi_id = $('.data').attr('data-id');
                // vehiculo:
                var vehi = $('.data').attr('value');
                /**/
                console.log("vehiculo: "+vehi);
                console.log("id: "+vehi_id);
                console.log("fecha: "+fecha);
                
                //var url = '/user/reportdayjson?id='+vehi_id+'&amp;fecha='+fecha 
                //console.log(url);
                //Eliminamos la tabla de reportes si existe:
                $('#tbreport').remove();
                var table = '<table id="tbreport" class="table table-hover table-condensed table-bordered"><thead><th>Fecha</th><th>Ubicación</th><th>Velocidad</th><head>'
               
                // AJAX
                jQuery.ajax({
                    url      : '/user/reportdayjson',
                    data     : { 'id':vehi_id , 'fecha':fecha },
                    type     : 'GET',
                    dataType : 'json',
                    success  : function(json){
                        var newElement = [];
                        jQuery.each(json, function(index, obj){
                            newElement.push('<tr><td>'+obj.fecha+'</td><td class="ubica" data-content="'+obj.ubicacion+'" data-position="'+obj.position+'">'+obj.ubicacion+'</td><td>'+obj.velocidad+' km/h </td></tr>');
                        });
                        console.log("Nuevo Elemento: "+newElement);
                        if (newElement == 0){
                            $('#alert').show().find('strong').text('No exiten reportes para este día.');
                            return null;
                        }
                        $('#report').after(table+'<tbody>'+newElement.join('')+'</tbody></table>');
                    },
                    error    : function(jqXHR, status, error){
                        console.log("Se produjo un error: " + error);
                    },
                    complete : function(jqXHR, status){
                        console.log("Petición terminada con estado: " + status);
                        console.log(jqXHR);
                        //* maps vehicles
                        maps_vehicle.init();
                    }
                }); 

        });
    }
}
