"""
File: API.py
Path: ./API/API.py
Description: HydrEAUviewer API for requesting hubEAU
Author: Sam Maxwell
Date: 02/2022
"""

## Imports ##

from flask import Flask, request, render_template, url_for
from numpy import empty
 
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

@API.route("/hydro/stations", methods=['POST', 'GET'])
def stations():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_object = data.Hydro_Stations(result)
        return render_template("hydro/stations.html", result = result, url_hubeau=data_object.get_url(), url_API=tb.args_to_request(url_for('hydro_data', domain='stations'),result))
    return render_template("hydro/stations.html")

@API.route("/hydro/elab", methods=['POST', 'GET'])
def elab():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_object = data.Hydro_Obs_Elab(result)
        return render_template("hydro/elab.html", result = result, url_hubeau=data_object.get_url(), url_API=tb.args_to_request(url_for('hydro_data', domain='elab'),result))
    return render_template("hydro/elab.html")

@API.route("/hydro/tr", methods=['POST', 'GET'])
def tr():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_object = data.Hydro_Obs_Tr(result)
        return render_template("hydro/tr.html", result = result, url_hubeau=data_object.get_url(), url_API=tb.args_to_request(url_for('hydro_data', domain='tr'),result))
    return render_template("hydro/tr.html")

@API.route("/hydro/<domain>/data")
def hydro_data(domain):
    result = request.args
    if domain == "stations":
        data_object = data.Hydro_Stations(result)
    if domain == "elab":
        data_object = data.Hydro_Obs_Elab(result)
    if domain == "tr":
        data_object = data.Hydro_Obs_Tr(result)
    return data_object.get_json() 
        

# ---------------------------------- Run API --------------------------------- #

if __name__ == "__main__":
    API.run(host='0.0.0.0', port=5000, debug=True)
    # API.run(debug=True)