"""
File: API.py
Path: ./API/API.py
Description: HydrEAUviewer API for requesting hubEAU
Author: Sam Maxwell
Date: 02/2022
"""

## Imports ##

from flask import Flask, request, render_template, url_for
 
# local modules #

import modules.toolbox as tb
# import modules.variables as var

# classes # 

import classes as data

# ------------------------------- Initialization ----------------------------- #

APP = Flask(__name__)

# ------------------------------------- APP ---------------------------------- #

@APP.route("/")
def home():
    return render_template("homePage.html")

# ------------------------------------- APP ---------------------------------- #

@APP.route("/APP")
def app():
    return render_template("app/homePageApp.html")

# ------------------------------------- API ---------------------------------- #

@APP.route("/API")
def api():
    return  render_template("api/homePageApi.html")

@APP.route("/API/hydro/stations", methods=['POST', 'GET'])
def stations():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_object = data.Hydro_Stations(result)
        return render_template("api/hydro/stations.html", result = result, url_hubeau=data_object.get_url(), url_API=tb.args_to_request(url_for('hydro_data', domain='stations'),result))
    return render_template("api/hydro/stations.html")

@APP.route("/API/hydro/elab", methods=['POST', 'GET'])
def elab():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_object = data.Hydro_Obs_Elab(result)
        return render_template("api/hydro/elab.html", result = result, url_hubeau=data_object.get_url(), url_API=tb.args_to_request(url_for('hydro_data', domain='elab'),result))
    return render_template("api/hydro/elab.html")

@APP.route("/API/hydro/tr", methods=['POST', 'GET'])
def tr():
    if request.method == 'POST':
        result = request.form.to_dict()
        data_object = data.Hydro_Obs_Tr(result)
        return render_template("api/hydro/tr.html", result = result, url_hubeau=data_object.get_url(), url_API=tb.args_to_request(url_for('hydro_data', domain='tr'),result))
    return render_template("api/hydro/tr.html")

@APP.route("/API/hydro/<domain>/data")
def hydro_data(domain):
    result = request.args
    if domain == "stations":
        data_object = data.Hydro_Stations(result)
    if domain == "elab":
        data_object = data.Hydro_Obs_Elab(result)
    if domain == "tr":
        data_object = data.Hydro_Obs_Tr(result)
    return data_object.get_json() 

# ---------------------------------- Run APP --------------------------------- #

if __name__ == "__main__":
    # APP.run(host='0.0.0.0', port=5000, debug=True)
    APP.run(debug=True)