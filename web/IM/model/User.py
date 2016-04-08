'''
Created on Mar 15, 2016

@author: wuw7

'''
from IM import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    owned_invs = db.relationship('Inventory', backref='ownerinvs', lazy='dynamic')
    
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
