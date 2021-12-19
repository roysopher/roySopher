from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

@app.route('/')
def home_func():  # put application's code here
    return render_template('info.html', name='Roy')

@app.route('/ass7')
def ass7():  # put application's code here
    return redirect(url_for('ass7'))

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
    profile={'Name': ' Roy', 'Family Name' : ' Sopher'},
    name = name,
    university=uni,
    second_name=second_name,
    degreas=['BSc', 'MSc'],
    hobies=('Football', 'Music', 'Chess'))


if __name__ == '__main__':
    app.run(debug=True)
