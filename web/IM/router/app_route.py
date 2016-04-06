'''
Created on Mar 15, 2016

@author: wuw7
'''
from flask import render_template, request, redirect, session, jsonify, Response, flash
from IM import app
from dao.UserDao import UserDao
from dao.InvDao import InvDao
from service.export_excel import Writer
from service.import_excel import Parser
from service.sse import ServerSentEvent

import os

import gevent
from gevent.queue import Queue

subscriptions = []

@app.route('/')
def welcome():
    return render_template('login.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['login-name']
        password = request.form['login-password']
        if UserDao.login(name, password):
            session['username'] = name
            return redirect('/home')
        else:
            return render_template('login.html', error = 'wrong login name or password')
    return render_template('login.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('inventory.html',
                            name = session.get('username'),
                            invs = InvDao.get_all_invs(),
                            title = "Hello",
                            task = "inventory")

@app.route('/inventory', methods=['GET'])
def inventory():
    return render_template('inventory.html',
                            name = session.get('username'),
                            invs = InvDao.get_all_invs(),
                            title = "Hello",
                            task = "inventory")
    
@app.route('/export-excel', methods=['GET'])
def export_excel():
    invs = InvDao.get_all_invs()
    data = []
    inv_args = []
    for inv in invs:
        inv_args.append(inv.tag)
        inv_args.append(inv.name)
        inv_args.append(inv.PN)
        inv_args.append(inv.SN)
        inv_args.append(inv.shipping)
        inv_args.append(inv.capital)
        inv_args.append(inv.disposition)
        inv_args.append(inv.status)
        inv_args.append(inv.owner)
        data.append(inv_args)
        inv_args=[]
    print data
    file_path = os.path.join(app.config['EXPORT_FOLDER'], 'export.xls')
    print file_path
    Writer.export_excel(data, file_path)
    return jsonify(result=True)

@app.route('/import-excel', methods=['POST'])
def import_excel():
    '''needs to check file type == xlsx etc. 
       if file exists, then server will overrides it by default. 
    '''
    file = request.files['choose-excel-file']
    print file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    print file_path
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    Parser.parse_by_row(file_path)
    # the imported inventories will be added to the database and appended on the page.
    return redirect('/inventory')  


@app.route('/add-inventory', methods=['POST'])
def add_inventory():
    tag = request.form.get('tag')
    name = request.form.get('name')
    PN = request.form.get('PN')
    SN = request.form.get('SN')
    ship = request.form.get('ship')
    cap = request.form.get('cap')
    dis = request.form.get('dis')
    #status = request.form.get('status')
    owner = request.form.get('owner')
    InvDao.add_inventory(tag, name, PN, SN, ship, cap, dis, "ok", owner)
    return jsonify(result=True)
    
@app.route('/edit-inventory', methods=['POST'])
def edit_inventory():
    inv_id = request.form.get('id')
    tag = request.form.get('tag')
    name = request.form.get('name')
    PN = request.form.get('PN')
    SN = request.form.get('SN')
    ship = request.form.get('ship')
    cap = request.form.get('cap')
    dis = request.form.get('dis')
    
    InvDao.update_inventory(inv_id, tag, name, PN, SN, ship, cap, dis)
    publish(inv_id, "has been edited.")
    
    return jsonify(result=True)

@app.route('/delete-inventory', methods=['POST'])
def delete_inventory():
    delete_ids = request.form.getlist('rows[]')
    print delete_ids
    b = InvDao.delete_inventory(delete_ids)
    return jsonify(result=b)

@app.route('/search-inventory', methods=['POST', 'GET'])    
def search_inventory():
    if request.method == 'POST':
        search_string = request.form['search-string']
        print search_string
        invs_list = InvDao.search_inventory(search_string)
        print invs_list
        return render_template('inventory.html',
                               name = session.get('username'),
                                invs = invs_list,
                                title = "Hello",
                                task = "inventory")
    else:
        return redirect('/inventory')
    
@app.route("/subscribe")
def subscribe():
    def gen():
        q = Queue()
        subscriptions.append(q)
        try:
            while True:
                result = q.get()
                ev = ServerSentEvent(str(result))
                yield ev.encode()
        except GeneratorExit: # Or maybe use flask signals
            subscriptions.remove(q)

    return Response(gen(), mimetype="text/event-stream")

def publish(inv_id, operation_msg):
    inv = InvDao.search_inventory_by_id(inv_id)
    current_user = session.get('username')
    users = 'admin'
    
    def notify():
        msg = str('The inventory named '+inv.name+' PN: '+inv.PN+' SN: '+inv.SN+ ';'+ users+ ';'+current_user+';'+operation_msg)
        for sub in subscriptions[:]:
            sub.put(msg)
    
    gevent.spawn(notify)