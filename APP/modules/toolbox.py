"""
File: toolbox.py
Path: ./API/modules/toolbox.py
Description: 
Author: Sam Maxwell
Date: 02/2022
"""

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