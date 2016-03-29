'''
Created on Aug 31, 2015
Start server
@author: wuw7

'''
from IM import app
from gevent.wsgi import WSGIServer

#this is important for flask to find router, ignore the warning.
from IM.router import app_route

if __name__ == '__main__':
#    app.run(debug=True)
    app.debug = True
    app.threaded = True
    server = WSGIServer(("", 5000), app)
    server.serve_forever()