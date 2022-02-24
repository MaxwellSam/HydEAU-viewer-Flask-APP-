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
import modules.variables as var

# ------------------------------- Initialization ----------------------------- #

API = Flask(__name__)

# ---------------------------------- Routes ---------------------------------- #

@API.route("/")
def root():
    return  render_template("homePage.html")

@API.route("/hydro/stations")
def stations():
    return render_template("stations/stations.html")

@API.route("/hydro/elab")
def elab():
    return render_template("hydro/hydroElab.html")

@API.route("/hydro/tr")
def tr():
    return render_template("hydro/hydroTr.html")

@API.route("/hydro/<string:domain>/result", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return result

# ---------------------------------- Run API --------------------------------- #

if __name__ == "__main__":
    API.run(debug=True)