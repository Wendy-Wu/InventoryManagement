'''
Created on Mar 15, 2016

@author: wuw7
'''
from IM import db
from model.Inventory import Inventory
import traceback

class InvDao():
    
    @staticmethod
    def get_all_invs():
        return Inventory.query.all()
    
    @staticmethod
    def add_inventory(tag, name, PN, SN, shipping, capital, disposition, state, owner=''):
        '''need try catch exception or just check if unique'''
        inv = Inventory(tag, name, PN, SN, shipping, capital, disposition, state, owner)
        try:
            db.session.add(inv)
            db.session.commit()
            return inv
        except:
            return None
        
    @staticmethod
    def delete_inventory(ids):
        invs=[]
        for an_id in ids:
            invs.append(InvDao.search_inventory_by_id(an_id))
        try:
            for inv in invs:
                db.session.delete(inv)
                db.session.commit()
            return True
        except:
            return False
        
    @staticmethod
    def update_inventory(ID, tag, name, PN, SN, shipping, capital, disposition):
        inv = InvDao.search_inventory_by_id(ID)
        inv.tag = tag
        inv.name = name
        inv.PN = PN
        inv.SN = SN
        inv.shipping = shipping
        inv.capital = capital
        inv.disposition = disposition
        db.session.commit()
        
    @staticmethod
    def update_state(ID, state):
        inv = InvDao.search_inventory_by_id(ID)
        inv.state = state
        db.session.commit()
    
    @staticmethod
    def update_user(ID, user):
        inv = InvDao.search_inventory_by_id(ID)
        inv.user = user
        db.session.commit()
        
    @staticmethod
    def update_owner(ID, owner):
        inv = InvDao.search_inventory_by_id(ID)
        inv.owner = owner
        db.session.commit()
        
    @staticmethod
    def search_inventory_by_id(search_id):
        return Inventory.query.filter_by(id = search_id).first()
    
    @staticmethod
    def search_inventory(search_string):
        results=[]
        temp=[]
        
        try:
            results.append(Inventory.query.filter_by(tag = search_string).all())
            results.append(Inventory.query.filter(Inventory.name.like('%'+search_string+'%')).all())
            results.append(Inventory.query.filter_by(PN = search_string).all())
            results.append(Inventory.query.filter_by(SN = search_string).all())
            results.append(Inventory.query.filter(Inventory.shipping.like('%'+search_string+'%')).all())
            results.append(Inventory.query.filter_by(capital = search_string).all())
            results.append(Inventory.query.filter(Inventory.disposition.like('%'+search_string+'%')).all())
            results.append(Inventory.query.filter_by(state = search_string).all())
            results.append(Inventory.query.filter_by(owner = search_string).all())
                        
        except Exception:
            traceback.print_exc()

        for result in results:
            if len(result) != 0:
                for item in result:
                    temp.append(item)
        
        results = temp
        return results
    
    @staticmethod
    def borrow(items, username):
        for item in items:
            InvDao.update_user(item, username)
            InvDao.update_state(item, 'used')
            
    @staticmethod
    def Return(items):
        for item in items:
            InvDao.update_user(item, '')
            InvDao.update_state(item, 'available')
            
    @staticmethod
    def scrap(items):
        for item in items:
            InvDao.update_state(item, 'scraped')
        
    @staticmethod
    def transfer(items, owner):
        for item in items:
            InvDao.update_owner(item, owner)