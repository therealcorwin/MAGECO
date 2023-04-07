from logging.config import fileConfig
from logging import getLogger
import configparser
from pathlib import Path 
import sqlite3 as sql

ROOT_APP_DIR = Path(__file__).resolve().parent

APP_DIR = ROOT_APP_DIR.parent
APP_DB_DIR = APP_DIR.joinpath("Db")
APP_DB_FILE = APP_DB_DIR.joinpath("Mageco.db")
APP_LOGGING_CONF_DIR = APP_DIR.joinpath("Conf")
APP_LOGGING_CONF_FILE = APP_LOGGING_CONF_DIR.joinpath("Logging.conf")
APP_CONF_DIR = APP_DIR.joinpath("Conf")
APP_CONF_FILE = APP_CONF_DIR.joinpath("Config.ini")


""" 

   INITIALISATION LOGGING

"""
# Enable logging
if  Path.is_file(APP_LOGGING_CONF_FILE):
    fileConfig(APP_LOGGING_CONF_FILE,encoding="utf_8")
    applog = getLogger("APPLOG")
    dbchecklog = getLogger("DBCHECK")
    dbdatalog = getLogger("DBDATA")
    applog.info("Lecture du fichier de configuration de la journalisation")
else:
    exit("Le fichier Logging.conf n'existe pas")

"""

    LECTURE FICHIER DE CONFIGURATION DE L'APPLICATION

"""
if Path.is_dir(APP_CONF_DIR):
    applog.info("Lecture du fichier de configuration")
    config_app = configparser.ConfigParser()
    config_app.read_file(open(APP_CONF_FILE,"r"))
else: 
   applog.critical("Le fichier config.ini n'existe pas")
   exit("Le fichier Config.ini n'existe pas")


"""

    INITIALISATION BD MAGECO

"""
if Path.is_file(APP_DB_FILE):
    applog.info("Base de données détectée")
else: 
    applog.error("Base de données absente")
    applog.info("Création du repertoire et de la base de données")
    try:
        Path.mkdir(APP_DB_DIR, exist_ok=True)
        DB_CONNECT = sql.connect(APP_DB_FILE)
        DB_CONNECT.close()
        applog.info("BDD Cree")
    except Exception as e:
        applog.error("une erreur c'est produite lors de la creation de la base de données : ")
        dbchecklog.error(e)
