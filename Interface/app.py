"""
File: app.py
Path: ./Interface/Flaskr/app.py
Description: Flask APP for hydrological data visualisation (data from hubEAU)
Author: Sam Maxwell
Date: 02/2022
"""

## Imports ##

from flask import Flask, request, render_template

# local modules #

# ------------------------------- Initialization ----------------------------- #

APP = Flask(__name__)

# ---------------------------------- Routes ---------------------------------- #

@APP.route("/")
def home():
    return render_template("homePage.html")

# ---------------------------------- Run API --------------------------------- #

if __name__ == "__main__":
    APP.run(debug=True)