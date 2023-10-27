from pygsheets import authorize
from .getconfig import return_config
from ..generateconfig import createConfig
import os

def ConnectGoogle(path=str): #path variable gives main folder's path. (folder that includes sheet.py)
    try:
        config = return_config(path+r"\Assets\Config\sheet_config.ini")
        gc = authorize(service_file=config["Credentials"]["CredsPath"])
        return gc 
    except: #If the program cannot authorize, it will check for the existence of a  
            #configuration file and, if it exists, delete it and recreate it.
        if os.path.exists(path+r"\Assets\Config\sheet_config.ini"):
            os.remove(path+r"\Assets\Config\sheet_config.ini")
            createConfig(path)

            config = return_config(path+r"\Assets\Config\sheet_config.ini")
            gc = authorize(service_file=config["Credentials"]["CredsPath"])
            return gc
        else:
            createConfig(path)

            config = return_config(path+r"\Assets\Config\sheet_config.ini")
            gc = authorize(service_file=config["Credentials"]["CredsPath"])
            return gc