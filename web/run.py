'''
Created on Aug 31, 2015
Start server
@author: wuw7

'''
from IM import app

#this is important for flask to find router, ignore the warning.
from IM.router import app_route

if __name__ == '__main__':
    app.run(debug=True)
