"""
File: API.py
Path: ./API/API.py
Description: HydrEAUviewer API for requesting hubEAU
Author: Sam Maxwell
Date: 02/2022
"""

## Imports ##

from flask import Flask, request, render_template
 
# local modules #

import modules.toolbox as tb
# import modules.variables as var

# classes # 

import classes as data

# ------------------------------- Initialization ----------------------------- #

API = Flask(__name__)

# ---------------------------------- Routes ---------------------------------- #

@API.route("/")
def home():
    return  render_template("homePage.html")

@API.route("/hydro/stations")
def stations():
    # if request.method == 'POST':
    #     result = request.form.to_dict()
    #     data_object = data.Hydro_Stations(result)
    #     return render_template("hydro/stations.html", result = result, url=data_object.get_url())
    return render_template("hydro/stations.html")

@API.route("/hydro/elab", methods=['POST', 'GET'])
def elab():
    # if request.method == 'POST':
    #     result = request.form.to_dict()
    #     data_object = data.Hydro_Obs_Elab(result)
    #     return render_template("hydro/elab.html", result = result, url=data_object.get_url())
    return render_template("hydro/elab.html")

@API.route("/hydro/tr", methods=['POST', 'GET'])
def tr():
    # if request.method == 'POST':
    #     result = request.form.to_dict()
    #     data_object = data.Hydro_Obs_Tr(result)
    #     return render_template("hydro/tr.html", result = result, url=data_object.get_url())
    return render_template("hydro/tr.html")

@API.route("/hydro/<domain>/result", methods=['POST', 'GET'])
def result(domain):
    if request.method == 'POST':
        result = request.form.to_dict()
        if domain == "stations":
            data_object = data.Hydro_Stations(result)
        elif domain == "elab":
            data_object = data.Hydro_Obs_Elab(result)
        elif domain == "tr":
            data_object = data.Hydro_Obs_Tr(result)
        
    # return render_template("hydro/{}.html".format(domain), result = result)
    return render_template("hydro/{}.html".format(domain), result = result, url=data_object.get_url())

# ---------------------------------- Run API --------------------------------- #

if __name__ == "__main__":
    # API.run(host='0.0.0.0', port=5000, debug=True)
    API.run(debug=True)