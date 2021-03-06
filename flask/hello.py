from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index page!'

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()
