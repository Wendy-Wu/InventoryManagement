'''
Created on Aug 31, 2015
Config database, environment variables, search path
@author: wuw7
'''
import os

SESSION_TYPE = 'sqlalchemy'

CONFIG_DIR = os.path.abspath(os.path.dirname(__file__))

UPLOAD_FOLDER = os.path.join(CONFIG_DIR, 'data', 'imported_files')
EXPORT_FOLDER = os.path.join(CONFIG_DIR, 'static', 'export_file')
# DB setting.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(CONFIG_DIR, 'data', 'IM.db')

#WHOOSH_BASE = "C:\\Python27\\Lib\\site-packages"
