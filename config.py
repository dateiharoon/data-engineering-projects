# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 18:23:32 2023

@author: Haroon
"""

import configparser
import pyodbc 
import mysql.connector
# connection to database
config = configparser.ConfigParser()
config.read(r'config.txt')

host  = config.get('DEFAULT','host')
database = config.get('DEFAULT','database')
username  = config.get('DEFAULT','username')
password  = config.get('DEFAULT','password')

db = mysql.connector.connect(
    host = host,
    database = database,
    user = username,
    password = password 
)
