from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/home')
def hello_world():  # put application's code here
    return redirect(url_for('hello'))

@app.route('/about')
def hello_world():  # put application's code here
    return redirect('/')

if __name__ == '__main__':
    app.run()
