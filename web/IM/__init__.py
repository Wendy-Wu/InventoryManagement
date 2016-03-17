'''
Created on Aug 31, 2015
Create and configure Flask, create session, DB instance
@author: wuw7
'''
import os, sys
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.session import Session
from config import CONFIG_DIR

# Create Flask instance.
app = Flask(__name__)

# Loading flask config.
sys.path.append(CONFIG_DIR)
app.config.from_object('config')
Session(app)

# Create DB instance.
db = SQLAlchemy(app)