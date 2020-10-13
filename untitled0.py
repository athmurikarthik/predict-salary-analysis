# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:59:34 2020

@author: User

 mkdir todo-api
 cd todo-api
 virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................done.
flask/bin/pip install flask
 mkdir todo-api
 cd todo-api
 virtualenv flask
New python executable in flask/bin/python
Installing setuptools............................done.
Installing pip...................don
pip install flask
import flask
flask.__version__
#C:\Users\User\Anaconda3\Scripts
from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
    return "Hello, World!"

if _name_ == '_main_':
    app.run(debug=True)
 