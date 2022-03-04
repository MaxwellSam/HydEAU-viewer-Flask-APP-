"""
File: toolbox.py
Path: ./API/modules/toolbox.py
Description: 
Author: Sam Maxwell
Date: 02/2022
"""

from classes import data_classes


def args_to_request(url, args):
    """
    Description: creat the HydroViewer API url from request argument to access data. 
        inputs:
            url: 
                type: str
                desc: url base cooresponding to the root to hydro_data()
            args
    """
    req = []
    for k in args:
        req.append("{}={}".format(k, args[k]))
    req_str = "&".join(req)
    return url+"?"+req_str

def get_list_stations(data_json):
    list_stations = []
    # return data_json.values()
    for station in data_json.values():
        # return station['code_station']
        if station['code_station'] not in list_stations:
            list_stations.append(station['code_station'])
        else:
            pass
    return list_stations

def get_list_stations_from_hydro_data(list_stations, data_type):
    # return data_type
    
    req = {
        "station":",".join(list_stations),
        "days_before":"3"
    }

    if data_type == "H":
        req["hydro_measure_tr"]="H"
        object_data = data_classes.Hydro_Obs_Tr(req)
    elif data_type == "Q":
        req["hydro_measure_tr"]="Q"
        object_data = data_classes.Hydro_Obs_Tr(req)
    elif data_type == "QmJ":
        req["hydro_measure_elab"]="QmJ"
        object_data = data_classes.Hydro_Obs_Elab(req)

    return get_list_stations(object_data.get_json())
    


