"""
File: variables.py
Path: ./modules/variables.py
Description: define variables for classes (url, fields, etc.) 
Author: Sam Maxwell
Date: 02/2022
"""
#####################################################################################
#                                        API                                        #
#####################################################################################

# ====================================== URL ====================================== #
"""
# Comment: 
hubEAU url bases for the different domains:
- Hydrological stations
- Real time hydrological data
- Elaborated hydrological data
"""

# -------------------------------- tools methods --------------------------------- #

def default_opsions_to_str(options):
    return "&".join(options)

def fields_to_str(fields):
    return "fields={}".format(",".join(fields))

def url_assembly(url_bases, options, fields):
    # return url_bases+"?{}&{}".format(default_opsions_to_str(options), fields_to_str(fields))
    if len(options) > 0: 
        return url_bases+"?{}&{}".format(default_opsions_to_str(options), fields_to_str(fields))
    else:
        return url_bases+"?{}".format(fields_to_str(fields))

# ------------------------------- common variables --------------------------------- #

timedate_convertion = {
    "days_before":1,
    "months_before":30, 
    "years_before":365
}

# ------------------------------ # hydro stations  # ------------------------------- #

## url bases ##

url_bases_hydro_stations = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations"

## default options ##

options_hydro_stations = [
    "en_service=true",
    "format=json"
]

## fields ##

fields_hydro_stations = [
    "code_station",
    "libelle_station",
    "type_station",
    "libelle_commune",
    "libelle_region",
    "date_ouverture_station",
    "longitude_station",
    "latitude_station"
] 

## translate keywords ##

translate_kw_hydro_stations = {
    "long":"longitude",
    "lat":"latitude",
    "dist":"distance",
    "stations":"code_entite"
}

## url hydro stations ## 

hydro_stations_url = url_assembly(url_bases_hydro_stations, options_hydro_stations, fields_hydro_stations)

# -------------------------------- # hydro elab  # --------------------------------- #

## url bases ## 

url_bases_hydro_elab = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/obs_elab"

## default options ## 

options_hydro_elab = [
    
]

## fields ##

fields_hydro_elab = [
    "code_station",
    "date_obs_elab",
    "date_prod",
    "grandeur_hydro_elab",
    "resultat_obs_elab"
]

## translate keywords ##

translate_kw_hydro_elab = {
    "station":"code_entite",
    "date_start_obs":"date_debut_obs_elab",
    "date_end_obs":"date_fin_obs_elab",
    "hydro_measure":"grandeur_hydro_elab",
    "days_before":"date_debut_obs_elab",
    "months_before":"date_debut_obs_elab",
    "years_before":"date_debut_obs_elab",
    "result_obs":"resultat_obs_elab"
}

## url hydro elab ##

hydro_elab_url = url_assembly(url_bases_hydro_elab, options_hydro_elab, fields_hydro_elab)

# -------------------------------- # hydro tr  # --------------------------------- #

## url bases ## 

url_bases_hydro_tr = "https://hubeau.eaufrance.fr/api/v1/hydrometrie/observations_tr"

## default options ## 

options_hydro_tr = [
    
]

## fields ##

fields_hydro_tr = [
    "code_station",
    "date_obs",
    "date_prod",
    "grandeur_hydro",
    "resultat_obs"
]

## translate keywords ##

translate_kw_hydro_tr = {
    "station":"code_entite",
    "date_start_obs":"date_debut_obs",
    "date_end_obs":"date_fin_obs",
    "hydro_measure":"grandeur_hydro",
    "days_before":"date_debut_obs",
    "months_before":"date_debut_obs",
    "years_before":"date_debut_obs",
    "time_step":"timestep",
    "result_obs":"resultat_obs"
}

## url hydro tr ##

hydro_tr_url = url_assembly(url_bases_hydro_tr, options_hydro_tr, fields_hydro_tr)


#####################################################################################
#                                        APP                                        #
#####################################################################################

# ============================== Map default variables ============================ #

default_lat = 44.837789
default_long = -0.57918
default_dist = 30
default_hydro_measures = {
    "water tide (H)":"H",
    "flow (Q)":"Q",
    "daily flow (QmJ)":"QmJ"
    }
default_data_hist = 5