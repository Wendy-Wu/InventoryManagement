'''
Created on Aug 31, 2015
Set User model for database 
@author: wuw7
'''
from IM import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    full_name = db.Column(db.String(64), unique=False, index=True)
    group = db.Column(db.Integer, unique=False, index=True)
    active = db.Column(db.Integer, unique=False, index=True)
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = password
        
    def __repr__(self):
        return '<User %r>' % (self.username)

    def verify_password(self, password):
        if self.password_hash != password:
            return False
        else:
            return True