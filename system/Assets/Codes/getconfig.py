import configparser

def return_config(path=str):
    config = configparser.ConfigParser()
    config.read(path)
    return config