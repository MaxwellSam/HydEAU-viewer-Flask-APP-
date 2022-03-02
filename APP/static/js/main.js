/**
 * FileName: main.js
 * date: 03/2022
 * Description: main script of HydrEAUviewer APP
 */

var long = document.getElementById("long")
var lat = document.getElementById("lat")
var dist = document.getElementById("dist")

// long.addEventListener('change', (long) => )

function generate_arg_req(args){
    var req = []
    args.map(arg => {
        req.push(arg.key+"="+arg.value)
    })
    return "?"+req.join("&")
}

function uploadmap(){
    var long = document.getElementById("long")
    var lat = document.getElementById("lat")
    var dist = document.getElementById("dist")
    
    let coord = [lat, long]

    let args_req = generate_arg_req({"long":long, "lat":lat, "dist":dist})

    fetch('/API/hydro/stations/data'+args_req) 
        .then((resp) => resp.json())
        .then((_data) => {
            loadMap(long, lat, _data)
        })
}