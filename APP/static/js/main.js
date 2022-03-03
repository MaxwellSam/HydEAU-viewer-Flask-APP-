/**
 * FileName: main.js
 * date: 03/2022
 * Description: main script of HydrEAUviewer APP
 */

var long = document.getElementById("long")
var lat = document.getElementById("lat")
var dist = document.getElementById("dist")

// long.addEventListener('change', (long) => )

const generate_arg_req = (args) => {
    var req = []
    args.map(arg => {
        req.push(arg.key+"="+arg.value)
    })
    return "?"+req.join("&")
}

const initializeMap = (long, lat, dist) => {
    let args_req = generate_arg_req({"long":long, "lat":lat, "dist":dist})

    fetch('/API/hydro/stations/data'+args_req) 
        .then((resp) => resp.json())
        .then((_data) => {
            loadMap(long, lat, _data)
        })
}

const uploadmap = () => {
    let long = document.getElementById("long")
    let lat = document.getElementById("lat")
    let dist = document.getElementById("dist")
    
    let coord = [lat, long]

    initializeMap(long, lat, dist)
}

const main = () => {
    var long = document.getElementById("long")
    var lat = document.getElementById("lat")
    var dist = document.getElementById("dist")

    initializeMap(long, lat, dist)

    [long, lat, dist].forEach( (element) => {
        element.addEventListner("change", uploadmap())
    });
}

// main()

loadMap()


