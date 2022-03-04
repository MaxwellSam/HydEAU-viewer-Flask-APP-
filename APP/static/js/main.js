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

const initializeMap = (long, lat, dist, hydro) => {
    let args_req = generate_arg_req({"long":long.value, "lat":lat.value, "dist":dist.value})
    console.log(args_req);
    console.log(`${window.origin}`+'/API/hydro/stations/data'+args_req);
    fetch(`${window.origin}`+'/API/hydro/stations/data'+args_req) 
        .then((resp) => resp.json())
        .then((_data) => {
            console.log(Object.values(_data))
            // console.log(Array.from(this.PaymentResponse.))
            loadMap(long.value, lat.value, hydro.value, _data)
        })
}

const uploadmap = () => {
    let long = document.getElementById("long")
    let lat = document.getElementById("lat")
    let dist = document.getElementById("dist")
    let hydro = document.getElementById("hydro_measure")
    
    let coord = [lat, long]

    initializeMap(long, lat, dist, hydro)
}

const main = () => {
    var long = document.getElementById("long")
    var lat = document.getElementById("lat")
    var dist = document.getElementById("dist")
    var hydro = document.getElementById("hydro_measure")
    console.log(hydro.value)
    initializeMap(long, lat, dist, hydro)

    // [long, lat, dist].forEach( (element) => {
    //     element.addEventListner("change", uploadmap())
    // });

    dist.addEventListner("change", uploadmap())
}

main()

// loadMap()


