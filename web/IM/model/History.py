'''
Created on Apr 7, 2016

@author: wuw7
'''
from IM import db

class History(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    invid = db.Column(db.Integer, index=True)
    username = db.Column(db.String(64), index=True)
    operation = db.Column(db.String(64))
    time = db.Column(db.String(64))
    
    def __init__(self, invid, username, operation, time):
        self.invid = invid
        self.username = username
        self.operation = operation
        self.time = time
    