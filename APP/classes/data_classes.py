"""
File: url_generator.py
Path: ./API/classes/url_generator
Description: Classes for converting request's arguments to url for hubEAU
Author: Sam Maxwell
Date: 02/2022
"""

## Imports ## 

from git import Object
import requests
import json
from datetime import date, timedelta

# local imports 

import modules.variables as var 
import modules.toolbox as tb

# =================================== HubEAU data hydro ====================================== #

class Hydro:
    """
    Class: Hydro
    Daughters: Hydro_Stations, Hydro_Obs
    Description: Generate hubEAU url to get stations around a coordinates point.
    """

    def fetch_json(self):
        """
        Description: Fetch data from hubEAU with the url and convert the response to json.
                     steps:
                     1) Fetch url => response
                     2) convert to json
                     3) select exclusively from json the object 'data' (contain data)
                     4) if multiple pages => fetch the next page and add new data to the dataset list.
                     5) return as dictionnary the final dataset.
            inputs:
                self.args: 
                    type: dict <str, str>
                    desc: dict which contain request arguments.
                self.url: 
                    type: str
        """
        try: 
            response = requests.get(self.url, verify=False)
        except requests.exceptions.RequestException as e:
            print("Error requests:", e)
        file = json.loads(response.text)
        data = file["data"]
        next = file["next"]
        if next != None:
            while next == None:
                try:
                    response_next = requests.get(next, verify=False)
                except requests.exceptions.RequestException as e:
                    print("Error requests \'next\'", e)
                file_next = json.loads(response_next.text) 
                data_next = file_next["data"]
                data += data_next
                next = file_next[next]
        self.data = {i:data[i] for i in range(len(data))}

    # ------------------ get ----------------------

    def get_json(self):
        return self.data
    
    def get_url(self):
        return self.url
        
# ------------------------------------- Hydro Stations --------------------------------------- #

class Hydro_Stations(Hydro):
    """
    Class: Hydro_Stations
    Parent: Hydro
    Description: Generate hubEAU url to get stations around a coordinates point.
    """
    url = var.hydro_stations_url
    translate_kw = var.translate_kw_hydro_stations

    def __init__(self, args):
        self.args = args
        self.__generate_url_hubeau()
        self.fetch_json()
    
    # ---------------- tools methods --------------------

    def __generate_url_hubeau(self):
        """
        Description: Generate the url for requestiong hubEAU from API request about hydrological stations information. 
                     It translate request's words and complete the url base.
            inputs:
                self.args: 
                    type: dict <str, str>
                    desc: dict which contain request arguments.
                self.url: 
                    type: str
        """
        for k in self.args.keys():
            try:
                self.url += "&{kw}={value}".format(kw=self.translate_kw[k], value=self.args[k])
            except ValueError as ve:
                print("Error: class \'Hydro_Stations\' method \'generate_url_hubeau' => key {} not valid.".format(k))
    
    # ------------------ get ----------------------

    def get_stations(self):
        return tb.get_list_stations(self.data)

    def get_stations_with_data(self, data_type):
        list_stations = tb.get_list_stations(self.data)
        return tb.get_list_stations_from_hydro_data(list_stations, data_type)
    
    # ------------- modif dataset -----------------

    def add_data_available(self):
        stations_Q = self.get_stations_with_data('Q')
        stations_H = self.get_stations_with_data('H')
        stations_QmJ = self.get_stations_with_data('QmJ')
        for station in self.data.values():
            station['hydro_measure_av'] = []
            if station['code_station'] in stations_Q:
                station['hydro_measure_av'].append('Q')
            if station['code_station'] in stations_H:
                station['hydro_measure_av'].append('H')
            if station['code_station'] in stations_QmJ:
                station['hydro_measure_av'].append('QmJ')

    def fetch_json(self):
        super().fetch_json()
        self.add_data_available()


# ----------------------------------- Hydro Observations --------------------------------------- #
    
class Hydro_Obs(Hydro):
    """
    Class: Hydro_Obs
    Parent: Hydro
    Daughters: Hydro_Obs_Elab, Hydro_Obs_Tr
    Description: Generate hubEAU for hydrological data.
    """
    timedate_conv = var.timedate_convertion

    # ---------------- tools methods --------------------

    def generate_url_hubeau(self):
        """
        Description: Generate the url for requestiong hubEAU from API request about hydrological data observations. 
                     It translate request's words and complete the url base.
            inputs:
                self.args: 
                    type: dict <str, str>
                    desc: dict which contain request arguments.
                self.url: 
                    type: str
        """
        for k in self.args.keys():
            try:
                if k in self.timedate_conv.keys():
                    date_to_start = date.today() - timedelta(days=int(self.args[k])*self.timedate_conv[k])
                    self.url += "&{}={}".format(self.translate_kw[k], date_to_start)
                else:
                    self.url += "&{}={}".format(self.translate_kw[k], self.args[k])
            except ValueError as ve:
                print("Error Value: class \'Hydro_Obs\' method \'__generate_url_hubeau\' type {} not valid ", ve)

    # ------------- modif dataset -----------------

    def rename_columns(self):
        for row in self.data.values():
            row["result_obs"] = row[self.translate_kw["result_obs"]]
            row["hydro_measure"] = row[self.translate_kw["hydro_measure"]]
            del row[self.translate_kw["result_obs"]]
            del row[self.translate_kw["hydro_measure"]]

    # ---------------- fetching -------------------

    def fetch_json(self):
        super().fetch_json()
        self.rename_columns()

    

class Hydro_Obs_Elab(Hydro_Obs):
    """
    Class: Hydro_Obs_Elab
    Parent: Hydro_Obs
    Type: Daughter
    Description: Generate hubEAU url to get elaborated hydrological data, convert and return data to json.
    """
    url = var.hydro_elab_url
    translate_kw = var.translate_kw_hydro_elab

    def __init__(self, args):
        self.args=args
        super().generate_url_hubeau()
        super().fetch_json()


class Hydro_Obs_Tr(Hydro_Obs):
    """
    Class: Hydro_Obs_Tr
    Parent: Hydro_Obs
    Type: Daughter
    Description: Generate hubEAU url to get hydrological data real time, convert and return data to json.
    """
    url = var.hydro_tr_url
    translate_kw = var.translate_kw_hydro_tr

    def __init__(self, args):
        self.args=args
        super().generate_url_hubeau()
        super().fetch_json()
        # super().__init__()
    
    # ------------- modif dataset -----------------

    # def rename_columns(self):
    #     for row in self.data.values():
    #         row["result_obs"] = row[self.translate_kw["result_obs"]]
    #         row["hydro_measure"] = row[self.translate_kw["hydro_measure"]]
    #         del row[self.translate_kw["result_obs"]]
    #         del row[self.translate_kw["hydro_measure"]]

# test 

# arg = {"station":"O965000101", "days_before":5}

# test = Hydro_Obs_Elab(arg)

        





