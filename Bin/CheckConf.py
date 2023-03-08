from logging.config import fileConfig
from logging import getLogger
import configparser
from os import path , getcwd, mkdir 
import sqlite3 as sql

APP_DIR = getcwd()
APP_DB_DIR = APP_DIR + "\Db\Mageco.db"
APP_LOGGING_CONF_DIR = APP_DIR + "\Conf\Logging.conf"
APP_CONF_DIR = APP_DIR + "\Conf\Config.ini"

""" 

   INITIALISATION LOGGING

"""
# Enable logging
if path.exists(APP_LOGGING_CONF_DIR):
    fileConfig(APP_LOGGING_CONF_DIR,encoding="utf_8")
    applog = getLogger("APPLOG")
    dbchecklog = getLogger("DBCHECK")
    dbdatalog = getLogger("DBDATA")
    applog.info("Lecture du fichier de configuration de la journalisation")
else:
    exit("Le fichier Logging.conf n'existe pas")

"""

    LECTURE FICHIER DE CONFIGURATION DE L'APPLICATION

"""
if path.exists(APP_CONF_DIR):
    applog.info("Lecture du fichier de configuration")
    config_app = configparser.ConfigParser()
    config_app.read_file(open(APP_CONF_DIR,"r"))
else: 
   applog.critical("Le fichier config.ini n'existe pas")
   exit("Le fichier Config.ini n'existe pas")


"""

    INITIALISATION BD MAGECO

"""
if path.exists(APP_DB_DIR):
    applog.info("Base de données détectée")
else: 
    applog.error("Base de données absente")
    applog.info("Création du repertoire et de la base de données")
    try:
        mkdir(APP_DIR + "\Db")
        DB_CONNECT = sql.connect(APP_DB_DIR)
        applog.info("BDD Cree")
    except Exception as e:
        applog.error("une erreur c'est produite lors de la creation de la base de données : ")
        dbchecklog.error(e)
