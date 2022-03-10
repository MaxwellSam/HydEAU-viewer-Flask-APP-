/**
 * FileName: map.js
 * date: 03/2022
 * Description: Map for hydrEAUviewer APP
 */

// -------------------------------- variables --------------------------------

// ----------------------------- Usefull methods -----------------------------

// ------------------------------- Graph Class -------------------------------

class GraphStation {
    // =============== Attributes ===================
    // Inputs user
    params_hydro = document.getElementById("params_hydro");
    // graph config 
    graphDiv = document.getElementById("graphDiv");
    // to check if initialized
    initialized = false;
    // line graph elementy
    lineGraph;

    constructor(){}

    // ------------- variables ----------------------
    hydro_measure_layout = {
        "H":"water tide",
        "Q":"flow",
        "QmJ":"daily flow"
    }
    // ------------- tools methods ------------------

    generate_arg_req = (args) => {
        let req = [];
        for (let k in args){
            req.push(k+"="+args[k]);
        } 
        return "?"+req.join("&");
    }
    
    generate_req_obs(code_station){
        let hydro_measure = this.params_hydro.hydro_measure.value;
        let days_before = this.params_hydro.days_before.value;
        let req = "/API/hydro/";
        let args = {
            "station":code_station,
            "hydro_measure":hydro_measure,
            "days_before":days_before 
        };
        if (hydro_measure == "H" || hydro_measure == "Q"){
            return req += "tr/data"+this.generate_arg_req(args);
        }
        else if (hydro_measure == "QmJ"){
            return req += "elab/data"+this.generate_arg_req(args);
        }
    }

    generate_layout(station){
        let layout = {
            title:`Evolution of ${this.hydro_measure_layout[this.params_hydro.hydro_measure.value]} for station ${station.libelle_station} (${station.code_station})`,
            xaxis: {
                title: `time`
            },
            yaxis: {
                title: `${this.hydro_measure_layout[this.params_hydro.hydro_measure.value]}`
            }
        };
        return layout;
    }

    // ------------ Initialization & refresh ------------------

    initialize(station){
        this.initialized = true;
        let url = `${window.origin}`+this.generate_req_obs(station.code_station)
        // test params 
        let infos_params = document.getElementById("info_params");
        infos_params.innerHTML = `<b>url</b><a href="${url}">${url}</a>`
        fetch(url) 
        .then((resp) => resp.json())
        .then((_data) => {
            let dataset = {
                x:[],
                y:[],
                type:'lines'
            }
            Object.values(_data).map((row) => {
                dataset.x.push(row.date_obs);
                dataset.y.push(row.result_obs);
            });
            this.lineGraph = Plotly.newPlot(this.graphDiv, [dataset], this.generate_layout(station))
        });
        
    }

    refresh(station){
        Plotly.purge(this.graphDiv);
        this.initialize(station);
    }

}