from flask import Flask, redirect, url_for, session, request
from flask import render_template

app = Flask(__name__)
app.secret_key = '123'

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
        if 'search_user' in request.args:
            search_user = request.args['search_user']
            return render_template('assignment9.html', username=session['username']
                                   , search_user=search_user
                                   , users=users)
        return render_template('assignment9.html', username=session['username'])
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
                           songs=('Pave it', 'Pointed', 'Deceptive', 'Eruptive Silence'))


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


if __name__ == '__main__':
    app.run(debug=True)


