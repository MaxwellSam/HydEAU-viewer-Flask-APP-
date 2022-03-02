/**
 * FileName: map.js
 * date: 03/2022
 * Description: Map for hydrEAUviewer APP
 */



// var = map = L.map('map').setView([]) 

function loadMap(long, lat, data_stations){
    // var map = L.map('map').setView([lat, long], 13)
    var map = L.map('map').setView([-0.57918, 44.837789], 13)
    data_stations.map(station => {
        L.marker([station.latitude_station, station.longitude_station]).addto(map)
    }) 
}