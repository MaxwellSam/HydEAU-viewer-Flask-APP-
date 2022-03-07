/**
 * FileName: map.js
 * date: 03/2022
 * Description: Map for hydrEAUviewer APP
 */

// -------------------------------- variables --------------------------------

// Markers color

var blueIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png',
	shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var redIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
	shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

// ----------------------------- Usefull methods -----------------------------

const attrib_color = (station, hydro) => {
    console.log(station.hydro_measure_av.includes(hydro))
    if (station.hydro_measure_av.includes(hydro)){
        return greenIcon
    } 
    else {
        return blueIcon
    }
}

const generate_arg_req = (args) => {
    console.log(args);
    var req = [];
    for (let k in args){
        console.log(k);
        req.push(k+"="+args[k])
    } 
    return "?"+req.join("&");
}

// -------------------------------- Creat Map --------------------------------

class MapStations {
    // =============== Inputs user ==================
    long = document.getElementById("long");
    lat = document.getElementById("lat");
    dist = document.getElementById("dist");
    hydro = document.getElementById("hydro_measure");
    // ============== Map elements ==================
    map = L.map('map');
    markersElements;

    constructor(){
        this.initialize();
    }

    // ================= Methods ====================
    addStations(url){
        // initialize markers group 
        this.markersElements = L.layerGroup().addTo(this.map);
        // fetch data and add station markers
        console.log(url)
        fetch(url) 
        .then((resp) => resp.json())
        .then((_data) => {
            Object.values(_data).map((station) => {
                L.marker(
                    [station.latitude_station, station.longitude_station],
                    {icon:attrib_color(station, this.hydro.value)}
                ).addTo(this.markersElements).bindPopup(station.libelle_station);
            });
        });
    }
    // ================= Methods ====================
    initialize(){
        // generate url for API requesting
        let url = `${window.origin}` + '/API/hydro/stations/data' + generate_arg_req({"long":this.long.value, "lat":this.lat.value, "dist":this.dist.value});
        // set Map view and tile
        this.map.setView([this.lat.value,this.long.value], 12);
        L.tileLayer(
            'https://api.maptiler.com/maps/hybrid/{z}/{x}/{y}.jpg?key=LHjfLlxpJcb3lcunyka2', 
            {
                attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
            }).addTo(this.map);
        // fetch data stations and add markers
        this.addStations(url);
    }

    refresh(){
        // generate url for API requesting
        let url = `${window.origin}` + '/API/hydro/stations/data' + generate_arg_req({"long":this.long.value, "lat":this.lat.value, "dist":this.dist.value});
        // reset Map view
        this.map.setView([lat.value,long.value], 12);
        // remove last markers
        this.map.removeLayer(this.markersElements);
        // fetch data stations and add markers
        this.addStations(url);
    }
}

// ------------------------------------- Inputs  --------------------------------------

var long = document.getElementById("long");
var lat = document.getElementById("lat");
var dist = document.getElementById("dist");
var hydro = document.getElementById("hydro_measure");

// ---------------------------------- Initialize Map  ---------------------------------- 

map = new MapStations()

// ----------------------------------- Event Listener  ---------------------------------

dist.addEventListener('change', () => {map.refresh()});
long.addEventListener('change', () => {map.refresh()});
lat.addEventListener('change', () => {map.refresh()});
hydro.addEventListener('change', () => {map.refresh()});





