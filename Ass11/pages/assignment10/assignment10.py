from idlelib import window

from flask import Flask, redirect
from flask import Blueprint
from interactDB import interact_db
from flask import render_template
from flask import request, flash
from tkinter import messagebox

import mysql.connector


app = Flask(__name__)
app.secret_key = "123"

assignment10 = Blueprint('/assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')

@assignment10.route('/assignment10')
def index():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['GET','POST'])
def insertUsers():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        input = "SELECT name FROM myDB.users WHERE name='%s';" % name
        answer = interact_db(query=input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into myDB.users (ID, name, email , password)\
                            value ('%s', '%s', '%s', '%s');" % (id, name, email, password)
            interact_db(query=query, query_type='commit')
            return redirect('/assignment10?p1=User-added')
        else:
            return redirect('/assignment10')
    return render_template('assignment10.html', req_method=request.method)


@assignment10.route('/update_User', methods=['GET', 'POST'])
def updateUsers():
        id = request.form['id']
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        query = " UPDATE myDB.users SET name='%s',email='%s' ,password='%s' WHERE id='%s';"%\
                (name, email, password, id)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10?p1=User-update')



@assignment10.route('/delete_user', methods=['POST'])
def deleteUsers():

    userId = request.form['id']
    check = "SELECT name FROM myDB.users WHERE id='%s';" % userId
    answer = interact_db(query=check, query_type='fetch')
    if len(answer) > 0:
        query = "delete from myDB.users where id='%s';" % userId
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10?p1=User-delete')
    else:
        return redirect('/assignment10?p1=User-notfound')


