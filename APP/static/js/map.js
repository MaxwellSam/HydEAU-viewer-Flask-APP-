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

const generate_arg_req = (args) => {
    console.log(args);
    var req = [];

    for (let k in args){
        console.log(k);
        req.push(k+"="+args[k])
    } 
    // args.map((arg) => {
    //     req.push(key+"="+value)
    // });
    console.log(req);
    return "?"+req.join("&");
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
    var map = L.map('map')
    map.setView([lat,long], 12)
    L.tileLayer('https://api.maptiler.com/maps/hybrid/{z}/{x}/{y}.jpg?key=LHjfLlxpJcb3lcunyka2', {
           attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>'
        }).addTo(map);

    add_markers(hydro, map, data_stations)
}

const initializeMap = (long, lat, dist, hydro) => {
    let args_req = generate_arg_req({"long":long.value, "lat":lat.value, "dist":dist.value})
    // console.log(args_req);
    // console.log(`${window.origin}`+'/API/hydro/stations/data'+args_req);
    fetch(`${window.origin}`+'/API/hydro/stations/data'+args_req) 
        .then((resp) => resp.json())
        .then((_data) => {
            // console.log(Object.values(_data))
            // console.log(Array.from(this.PaymentResponse.))
            loadMap(long.value, lat.value, hydro.value, _data)
        })
}

const reloadmap = () => {
    let long = document.getElementById("long")
    let lat = document.getElementById("lat")
    let dist = document.getElementById("dist")
    let hydro = document.getElementById("hydro_measure")

    // map.off()
    // let map = document.getElementById('map');
    // let parent = map.parentNode
    // map.remove()
    // let new_el = document.createElement('div')
    // new_el.id = "map"
    // parent.appendChild(new_el)
    // let map = document.getElementById('map');
    // let firstChild = map.firstChild;
    // console.log(firstChild)
    // // map.querySelectorAll('*').forEach(n => n.remove());
    // map.removeChild(map.firstChild);
    // firstChild = map.firstChild;
    // console.log(firstChild)
    // initializeMap(map, long, lat, dist, hydro)
    initializeMap(long, lat, dist, hydro)
}

// ---------------------------------- main ----------------------------------

var long = document.getElementById("long");
var lat = document.getElementById("lat");
var dist = document.getElementById("dist");
var hydro = document.getElementById("hydro_measure");

// var map = L.map('map');

initializeMap(long, lat, dist, hydro);

// dist.addEventListener('change', () => {reloadmap(), test_event()});
// // dist.addEventListner('change', uploadmap(map));
// long.addEventListener('change', () => {reloadmap(), test_event()});
// lat.addEventListener('change', () => {reloadmap(), test_event()});
// hydro.addEventListener('change', () => {reloadmap(); test_event();});

// test eventListener

var test_1 = document.getElementById('test-1')
var test_2 = document.getElementById('test-2')
var test_3 = document.getElementById('test-3')
var test_4 = document.getElementById('test-4')

const test_event = () => {
    test_1.innerHTML = "long = "+long.value;
    test_2.innerHTML = "lat = "+lat.value;
    test_3.innerHTML = "dist = "+dist.value;
    test_4.innerHTML = "hydro = "+hydro.value;
}

dist.addEventListener('change', () => test_event());
long.addEventListener('change', () => test_event());
lat.addEventListener('change', () => test_event());
hydro.addEventListener('change', () => test_event());




