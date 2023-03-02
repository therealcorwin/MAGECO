from logging.config import fileConfig
from logging import getLogger
import configparser
from os import path



""" 

   INITIALISATION LOGGING

"""
# Enable logging
if path.exists("Logging.conf"):
    fileConfig("Logging.conf",encoding="utf_8")
    applog = getLogger("APPLOG")
    dbchecklog = getLogger("DBCHECK")
    dbdatalog = getLogger("DBDATA")
    applog.info("Lecture du fichier de configuration de la journalisation")
else:
    exit("Le fichier Logging.conf n'existe pas")

"""

    LECTURE FICHIER DE CONFIGURATION DU BOT

"""
if path.exists("config.ini"):
    applog.info("Lecture du fichier de configuration")
    config_bot = configparser.ConfigParser()
    config_bot.read_file(open("config.ini","r"))
else: 
   applog.critical("Le fichier config.ini n'existe pas")
   exit("Le fichier config.ini n'existe pas")
