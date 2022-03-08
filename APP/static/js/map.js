/**
 * FileName: map.js
 * date: 03/2022
 * Description: Map for hydrEAUviewer APP
 */

// -------------------------------- variables --------------------------------

// zoom 
var zoom = 9

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

var greyIcon = new L.Icon({
	iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-grey.png',
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
    if (station.hydro_measure_av.includes(hydro)){
        return greenIcon;
    } 
    else {
        return greyIcon;
    }
}

const generate_arg_req = (args) => {
    var req = [];
    for (let k in args){
        req.push(k+"="+args[k]);
    } 
    return "?"+req.join("&");
}

const place_graph_on_page = (station) => {
    let graph = document.getElementById('graph');
    let info_station = document.getElementById('info_station')
    graph.style.display = "block";
    info_station.innerHTML = `<b>station:</b> ${station.libelle_station}<br/><b>code:</b> ${station.code_station}`
    
}

// -------------------------------- Map Class --------------------------------

class MapStations {
    // =============== Attributes ===================
    // Inputs user
    params = document.getElementById("params");
    // Map elements 
    map = L.map('map');
    markersElements;

    // =============== Constructor ==================
    constructor(){
        this.initialize();
    }

    // ================= Methods ====================
    addStations(url){
        // save the last marker selected to remove blue color
        let last_marker;
        // initialize markers group 
        this.markersElements = L.layerGroup().addTo(this.map);
        // fetch data and add station markers
        fetch(url) 
        .then((resp) => resp.json())
        .then((_data) => {
            Object.values(_data).map((station) => {
                let marker = L.marker(
                    [station.latitude_station, station.longitude_station],
                    {icon:attrib_color(station, this.params.hydro_measure.value)}
                )
                .addTo(this.markersElements)
                .bindPopup("<b>"+station.libelle_station+"</b><br/>"+station.code_station)
                .on('click', () => {
                    if (marker.getIcon() == greenIcon){
                        if (last_marker != null){
                            last_marker.setIcon(greenIcon);
                        }
                        // infos station selected
                        let info_Station_html = document.getElementById('station_selected');
                        last_marker = marker;
                        info_Station_html.innerHTML = 
                            ` <h4 class="p-2">Station selected</h4>
                            <p>
                                <b>libelle:</b> ${station.libelle_station}<br/>
                                <b>code:</b> ${station.code_station}<br/>
                                <b>data available:</b> ${station.hydro_measure_av}
                            </p> 
                            <button id="button_graph" type="button" class="btn btn-dark">See graph</button> 
                            `;
                        // graph station selected
                        let button_graph = document.getElementById('button_graph');
                        button_graph.addEventListener("click", (event) => {
                            if (event.detail)
                            place_graph_on_page(station); 
                            console.log("clicked on button")
                        });
                        console.log("ok")
                        marker.setIcon(blueIcon)
                    }
                    console.log(marker.getIcon())
                    console.log(station.code_station)
                });
            });
        });
    }
    
    // -------------- init & refresh -----------------
    initialize(){
        // generate url for API requesting
        let url = `${window.origin}` + '/API/hydro/stations/data' + generate_arg_req({"long":this.params.long.value, "lat":this.params.lat.value, "dist":this.params.dist.value});
        // set Map view and tile
        this.map.setView([this.params.lat.value,this.params.long.value], zoom);
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
        let url = `${window.origin}` + '/API/hydro/stations/data' + generate_arg_req({"long":this.params.long.value, "lat":this.params.lat.value, "dist":this.params.dist.value});
        // reset Map view
        this.map.setView([this.params.lat.value,this.params.long.value], zoom);
        // remove last markers
        this.map.removeLayer(this.markersElements);
        // fetch data stations and add markers
        this.addStations(url);
    }
}

// ------------------------------------- Inputs  --------------------------------------

var params = document.getElementById("params")
var submit_params = document.getElementById("submit_params")

// ---------------------------------- Initialize Map  ---------------------------------- 

map = new MapStations()

// ----------------------------------- Event Listener  ---------------------------------

submit_params.addEventListener('click', () => {map.refresh()})




