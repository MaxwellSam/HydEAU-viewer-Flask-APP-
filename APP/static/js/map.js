/**
 * FileName: map.js
 * date: 03/2022
 * Description: Map for hydrEAUviewer APP
 */

// -------------------------------- variables --------------------------------

// Markers color

var blueIcon = new L.Icon({
	iconUrl: 'img/marker-icon-2x-blue.png',
	shadowUrl: 'img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var redIcon = new L.Icon({
	iconUrl: 'img/marker-icon-2x-red.png',
	shadowUrl: 'img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

var greenIcon = new L.Icon({
	iconUrl: 'img/marker-icon-2x-green.png',
	shadowUrl: 'img/marker-shadow.png',
	iconSize: [25, 41],
	iconAnchor: [12, 41],
	popupAnchor: [1, -34],
	shadowSize: [41, 41]
});

// ----------------------------- Usefull methods -----------------------------

const attrib_color = (station, hydro) => {
    if (hydro in station.hydro_measure_av){
        return greenIcon
    } 
    else {
        return redIcon
    }
}

const add_markers = (hydro, map, data_stations) => {
    
    Object.values(data_stations).map((station) => {
        L.marker(
            [station.latitude_station, station.longitude_station],
            {Icon:attrib_color(station, hydro)}
        ).addTo(map).bindPopup(station.libelle_station)
    })
}

// -------------------------------- Creat Map --------------------------------

/**
 * load the map and add markers according to data stations
 * @param {string} long longitude for map center
 * @param {string} lat latitude for map center
 * @param {JSON} data_stations data of stations to display on map
 */
const loadMap = (long, lat, hydro, data_stations) => {
    console.log("--->", hydro);
    var map = L.map('map').setView([lat,long], 12)
    L.tileLayer('https://api.maptiler.com/maps/hybrid/{z}/{x}/{y}.jpg?key=LHjfLlxpJcb3lcunyka2', {
           attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
        }).addTo(map);
    
    // L.marker(
    //     [lat, long],
    //     {Icon:redIcon}
    // ).addTo(map)

    add_markers(hydro, map, data_stations)
    // for (let k in data_stations){
    //     // console.log(data_stations[k].latitude_station)
    //     // let marker = L.marker([data_stations[k].latitude_station, data_stations[k].longitude_station])
    //     // marker.addTo(map)
    //     L.marker([data_stations[k].latitude_station, data_stations[k].longitude_station]).addTo(map)
    // }
}