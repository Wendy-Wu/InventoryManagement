'''
Created on Apr 7, 2016

@author: wuw7
'''
from IM import db
from model.History import History

import traceback

class HistoryDao():
    
    @staticmethod
    def get_all_his():
        return History.query.all()
    
    @staticmethod
    def add_record(invids, username, operation, time):
        '''need try catch exception or just check if unique'''
        for invid in invids:
            record = History(invid, username, operation, time)
            try:
                db.session.add(record)
            except Exception:
                traceback.print_exc()
        db.session.commit()

        