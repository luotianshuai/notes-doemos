#!/usr/bin/env python
#-*- coding:utf-8 -*-


from flask import Flask,render_template,request
app = Flask(__name__)

def shuaige():
    return "<h1>LuoTianShuai</h1>"

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('/login.html',name=shuaige)

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)


app.run()