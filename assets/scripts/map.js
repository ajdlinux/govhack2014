var map;

var heatmapLayer = new google.maps.KmlLayer(null);
var pointLayers = [];

var sliders = [
    {'id': 'income',
     'name': 'Income',
     'low_label': 'Low',
     'high_label': 'High'},
    {'id': 'population', // TODO density
     'name': 'Population', // TODO density
     'low_label': 'Low',
     'high_label': 'High'},
    {'id': 'age',
     'name': 'Median Age',
     'low_label': 'Younger',
     'high_label': 'Older'},
    {'id': 'household',
     'name': 'Household Type',
     'low_label': 'Singles/Couples',
     'high_label': 'Families'},
    {'id': 'schools',
     'name': 'Distance to Schools',
     'low_label': 'Closer',
     'high_label': 'Further'},
    {'id': 'hospitals',
     'name': 'Distance to Hospitals',
     'low_label': 'Closer',
     'high_label': 'Further'}
];

// From http://stackoverflow.com/questions/5448545/how-to-retrieve-get-parameters-from-javascript
function loadPageVar(val) {
    var result = "Not found",
        tmp = [];
    location.search
    //.replace ( "?", "" ) 
    // this is better, there might be a question mark inside
    .substr(1)
        .split("&")
        .forEach(function (item) {
        tmp = item.split("=");
        if (tmp[0] === val) result = decodeURIComponent(tmp[1]);
    });
    return result;
}

function initialize() {
    var mapOptions = {
        center: new google.maps.LatLng(-35.3075, 149.1244),
        zoom: 11
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
				  mapOptions);
    displaySliders();
    addPointLayer('schools');
    addPointLayer('hospitals');
    loadHeatmapLayer();
}

function addPointLayer(layerName) {
    pointLayers[layerName] = [new google.maps.KmlLayer({
	url: 'http://' + window.location.host + '/pointlayer.kml?layer=' + layerName,
	preserveViewport: true,
	suppressInfoWindows: true,
	map: map}), true];
}

function displaySliders() {
    sliders.forEach(function (slider) {
	$('#sliders').append('<div class="slider"><label for="slider_' + slider['id'] + '">' + slider['name'] + '</label><input name="slider_' + slider['id'] + '" type="range" min="0" max="6" onchange="loadHeatmapLayer()" /></div>');
	
	$('#sliders-advanced').append('<div class="slider"><label for="slider_' + slider['id'] + '">' + slider['name'] + ' Care Factor</label><input name="slider_' + slider['id'] + '_weight" type="range" min="0" max="6" onchange="loadHeatmapLayer()" /></div>');

	if (loadPageVar(slider['id'])) {
	    $('[name=slider_' + slider['id'] + ']')[0].value = loadPageVar(slider['id']);
	}
	if (loadPageVar(slider['id'] + '_weight')) {
	    $('[name=slider_' + slider['id'] + '_weight]')[0].value = loadPageVar(slider['id'] + '_weight');
	}
    });
}

function loadHeatmapLayer() {
    params = {}
    sliders.forEach(function (slider) {
	params[slider['id'] + '_val'] = $('[name=slider_' + slider['id'] + ']')[0].value;
	params[slider['id'] + '_weight'] = $('[name=slider_' + slider['id'] + '_weight]')[0].value;
    });
    newHeatmapUrl = 'http://' + window.location.host + '/heatmap.kml?' + $.param(params);
    heatmapLayer.setMap(null);
    heatmapLayer = new google.maps.KmlLayer({
	url: newHeatmapUrl,
	preserveViewport: true,
	suppressInfoWindows: true,
	map: map});


    if ($('[name=slider_schools_weight]')[0].value == 0) {
	if (pointLayers['schools'][1]) {
	    pointLayers['schools'][0].setMap(null);
	}
    } else {
	if (pointLayers['schools'][1]) {
	    pointLayers['schools'][0].setMap(map);
	}
    }

    if ($('[name=slider_hospitals_weight]')[0].value == 0) {
	if (pointLayers['hospitals'][1]) {
	    pointLayers['hospitals'][0].setMap(null);
	}
    } else {
	if (pointLayers['hospitals'][1]) {
	    pointLayers['hospitals'][0].setMap(map);
	}
    }


}

google.maps.event.addDomListener(window, 'load', initialize);
