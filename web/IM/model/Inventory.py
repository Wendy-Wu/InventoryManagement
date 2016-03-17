'''
Created on Mar 15, 2016

@author: wuw7

'''
from IM import db

class Inventory(db.Model):
    __searchable__ = ['tag', 'name']
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    tag = db.Column(db.String(64), index=True)
    name = db.Column(db.String(64), index=True)
    PN = db.Column(db.String(64), index=True)
    SN = db.Column(db.String(64), unique=True, index=True)
    shipping = db.Column(db.String(64))
    capital = db.Column(db.String(64))
    disposition = db.Column(db.String(128))
    status = db.Column(db.String(64), index=True)
    owner = db.Column(db.String(64), db.ForeignKey('user.username'))
    user = db.relationship('User')
    
    
    def __init__(self, tag, name, pn, sn, ship, cap, dis, sta, owner=''):
        self.tag = tag
        self.name = name
        self.PN = pn
        self.SN = sn
        self.shipping = ship
        self.capital = cap
        self.disposition = dis
        self.status = sta
        self.owner = owner
    
    def __repr__(self):
        return '<Inventory %r:%r>' % (self.PN, self.SN)
    
    def to_json(self):
        return{
               'id':self.id,
               'SN':self.SN,
               'PN':self.PN,
               'tag':self.tag
               }