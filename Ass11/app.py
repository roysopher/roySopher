from flask import Flask, redirect, url_for, session, request
from flask import render_template
from interactDB import interact_db
import json
import requests

app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')

users = {'user1': {'name': 'Li', 'last name': 'Ron', 'Email': 'liron@gmail.com'},
         'user2': {'name': 'Avi', 'last name': 'Hen', 'Ron': 'aviron@gmail.com'},
         'user3': {'name': 'Ha', 'last name': 'Ron', 'Email': 'haron@gmail.com'},
         'user4': {'name': 'Beri', 'last name': 'Tsakala', 'Email': 'beritsakala@gmail.com'},
         'user5': {'name': 'Noor', 'last name': 'It', 'Email': 'noorit@gmail.com'},
         }



@app.route('/')
def home_func():  # put application's code here
    return render_template('info.html', name='Roy')


@app.route('/ass7')
def ass7():  # put application's code here
    return redirect(url_for('ass7'))


@app.route('/assignment9', methods=['GET', 'POST'])
def login_func():  # put application's code here
    if request.method == 'GET':
        if session['username']:
            if 'search_user' in request.args:
                search_user = request.args['search_user']
                return render_template('assignment9.html', username=session['username']
                                       , search_user=search_user
                                       , users=users)
            return render_template('assignment9.html', users=users, username=session['username'])
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_login'] = True
            return render_template('assignment9.html', username=username, users=users)
        else:
            return render_template('assignment9.html')


@app.route('/logout')
def logout_func():  # put application's code here
    session['username'] = ''
    return render_template('info.html')


@app.route('/songs', methods=['GET', 'POST'])
def songs_func():  # put application's code here
    return render_template('songs.html',
                           songs=('Pave it', 'Pointed', 'Deceptive', 'Eruptive Silence', 'Dance Monkey remix'))


@app.route('/info', methods=['GET', 'POST'])
def about_func():  # put application's code here
    name = 'Roy'
    second_name = 'Sopher'
    uni = 'BGU'
    return render_template('profile.html',
                           profile={'Name': ' Roy', 'Family Name': ' Sopher'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc'],
                           hobies=('Football', 'Music', 'Chess'))

@app.route('/assignment11')
def assignment11_func():  # put application's code here
    return render_template('assignment11.html', non="non")

def get_users(index):
    res = requests.get(f'https://reqres.in/api/users/{index}')
    return res.json()

@app.route('/assignment11/users')
def json_func():  # put application's code here
    dictionary = {}
    query = "SELECT * FROM myDB.users;"
    answer = interact_db(query=query, query_type='fetch')
    for user in answer:
        dictionary[f'user_{user.id}'] = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
    return render_template('assignment11.html', answer=dictionary, non="non")

@app.route('/assignment11/outer_source',  methods=['post'])
def outer_source_func():
    if "frontend" in request.form:
        num = int(request.form['frontend'])
        return render_template('assignment11.html', frontend=num)
    elif "backend" in request.form:
        num = int(request.form["backend"])
        user = get_users(num)
        return render_template('assignment11.html', backend=user)
    else:
        return render_template('assignment11.html')


from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

if __name__ == '__main__':
    app.run(debug=True)


