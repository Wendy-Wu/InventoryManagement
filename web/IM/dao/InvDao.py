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
    def add_inventory(tag, name, PN, SN, shipping, capital, disposition, status, owner=''):
        '''need try catch exception or just check if unique'''
        inv = Inventory(tag, name, PN, SN, shipping, capital, disposition, status, owner)
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
    def search_inventory_by_id(search_id):
        return Inventory.query.filter_by(id = search_id).first()
    
    @staticmethod
    def search_inventory(search_string):
        results=[]
        try:
            results.append(Inventory.query.filter_by(tag = search_string).all())
            results.append(Inventory.query.filter_by(name = search_string).all())
            results.append(Inventory.query.filter_by(PN = search_string).all())
            results.append(Inventory.query.filter_by(SN = search_string).all())
            results.append(Inventory.query.filter_by(shipping = search_string).all())
            results.append(Inventory.query.filter_by(capital = search_string).all())
            results.append(Inventory.query.filter_by(disposition = search_string).all())
            results.append(Inventory.query.filter_by(status = search_string).all())
            results.append(Inventory.query.filter_by(owner = search_string).all())
                        
        except Exception:
            traceback.print_exc()

        return results