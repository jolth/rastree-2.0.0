/*global $, Modernizr, google*/

var taitems = (function() {

	"use strict";

	var d = new Date(), status, today = {}, map, correctLocation, isSmallDevice = false;

	if((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i))) {
		isSmallDevice = true;
	}
	
	var australianOffset = -11;
	var hour = 3600000;
	var localOffset = d.getTimezoneOffset()/60;
	var taitTime = new Date();
	var adjustment = (australianOffset-localOffset)*hour;
	taitTime.setTime(taitTime-adjustment);

	//oh, i see you're trying to figure out how i did this. cool.
	//just fyi, all of the locations (except my workplace) are approximate lat/lng
	//i wouldn't be completely silly and put my home address in the code below...
	var locations = [
		{
			message: "I'm probably at home.",
			weekday: null,
			start: null,
			end: null,
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Murrumbeena, Victoria, Australia"
		},
		{
			message: "I'm probably asleep.",
			weekday: null,
			start: "11pm",
			end: "7:15am tomorrow",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Murrumbeena, Victoria, Australia"
		},
		{
			message: "I'm probably asleep.",
			weekday: null,
			start: "12am",
			end: "7:15am",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Murrumbeena, Victoria, Australia"
		},
		{
			message: "I'm probably commuting.",
			weekday: true,
			start: "8am",
			end: "8:45am",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Murrumbeena, Victoria, Australia"
		},
		{
			message: "I'm probably commuting.",
			weekday: true,
			start: "5:30pm",
			end: "6:30pm",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Murrumbeena, Victoria, Australia"
		},
		{
			message: "I'm probably at work.",
			weekday: true,
			start: "9am",
			end: "5:30pm",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Kiandra IT, Melbourne"
		},
		{
			message: "I'm probably coding.",
			weekday: null,
			start: "7pm",
			end: "9pm",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Murrumbeena, Victoria, Australia"
		},
		{
			message: "I'm probably at a cafe.",
			weekday: false,
			start: "10am",
			end: "1pm",
			lat: 5.06782,
			lng: -75.50245,
			toGoogle: "Carnegie, Victoria, Australia"
		}
	];
	
	if (d.getDay() === 0 || d.getDay() === 6) {
		today.weekday = false;   
	} else {
		today.weekday = true;   
	}
	
	$(locations).each(function(i,item) {
		var startTime = null, endTime = null;
		if (today.weekday === item.weekday || item.weekday === null) {
			if (item.start !== null) {
				startTime = Date.parse(item.start);
			}
			if (item.end !== null) {
				endTime = Date.parse(item.end);
			}
			if (startTime !== null && endTime !== null) {
				if (startTime < d && endTime > d) {
					status = item.message;
					correctLocation = item;   
				}
			} else {
				correctLocation = item;
				status = item.message; 
			}
		}
	});
	
	$(function() {
	
		$("#whereabouts").html("<span>" + status + "</span>");

		if (isSmallDevice) {
			return;
		}
		
		var latlng = new google.maps.LatLng(correctLocation.lat,correctLocation.lng);
		
		var myOptions = {
			zoom: 15,
			center: latlng,
			disableDefaultUI: true,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		};
		
		map = new google.maps.Map(document.getElementById("map"), myOptions);
		
		$("#whereabouts").twipsy();

		$("#openMap").removeAttr("disabled").click(function(e) {
			e.preventDefault();
			document.location = "http://maps.google.com/maps?q=" + correctLocation.toGoogle;
		});
	
	});
	
	return { };
	
})();
