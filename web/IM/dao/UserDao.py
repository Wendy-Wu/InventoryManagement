'''
Created on Mar 15, 2016

@author: wuw7
'''
from IM import db
from model.User import User

class UserDao():
    
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def delete_a_user(name):
        return True
        
    @staticmethod
    def search_user(name):
        return User.query.filter_by(username = name).first()
    
    @staticmethod
    def login(name, password):
        user = UserDao.search_user(name)
        if user:
            return user.verify_password(password)
        else:
            return False
