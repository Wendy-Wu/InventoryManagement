'''
Created on Mar 15, 2016

@author: wuw7
'''
from flask import render_template, request, redirect, session, jsonify
from IM import app
from dao.UserDao import UserDao
from dao.InvDao import InvDao
from service.export_excel import Writer


import os

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
    return render_template('mainbody.html',
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
    return jsonify(result=True)

@app.route('/delete-inventory', methods=['POST'])
def delete_inventory():
    delete_ids = request.form.getlist('rows[]')
    print delete_ids
    b = InvDao.delete_inventory(delete_ids)
    return jsonify(result=b)