"""
File: url_generator.py
Path: ./API/classes/url_generator
Description: Classes for converting request's arguments to url for hubEAU
Author: Sam Maxwell
Date: 02/2022
"""

## Imports ## 

import requests
import json
from datetime import date, timedelta

# local imports 

import classes.variables as var 

# =================================== HubEAU data hydro ====================================== #

class Hydro:
    """
    Class: Hydro
    Daughters: Hydro_Stations, Hydro_Obs
    Description: Generate hubEAU url to get stations around a coordinates point.
    """
    def url_hubeau_to_json(self):
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
        return {i:data[i] for i in range(len(data))}
    
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
    
    
class Hydro_Obs(Hydro):
    """
    Class: Hydro_Obs
    Parent: Hydro
    Daughters: Hydro_Obs_Elab, Hydro_Obs_Tr
    Description: Generate hubEAU for hydrological data.
    """
    timedate_conv = var.timedate_convertion
    
    def __init__(self):
        self.__generate_url_hubeau()

    def __generate_url_hubeau(self):
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
        super().__init__()

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
        super().__init__()

        

# test 

args = {
    "long":"-0.57918",
    "lat":"44.837789",
    "dist":"1000"
    } 

args2 = {
    "stations":"A021005050",
    "days_before":"5"
}         

## Test ## note : works if => import variables as var (not import classes.variables as var)

# obj = Hydro_Stations(args)
# print(obj.get_url())
# # print(obj.url_hubeau_to_json())
# obj2 = Hydro_Obs_Elab(args2)
# print("\n", obj2.get_url())

# print("\n", obj2.url_hubeau_to_json())

# obj3 = Hydro_Obs_Tr(args2)

# print("\n", obj3.get_url())
# print("\n", obj3.url_hubeau_to_json())




