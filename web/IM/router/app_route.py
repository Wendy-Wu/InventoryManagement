'''
Created on Mar 15, 2016

@author: wuw7
'''
from flask import render_template, request, redirect, session
from IM import app
from dao.UserDao import UserDao
from dao.InvDao import InvDao

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
                            invs = InvDao.get_all_invs())
