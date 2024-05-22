from markupsafe import escape
from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def greet(name):
    return f"Hello, {escape(name)}!"

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello, World'

if __name__ == '__main__':
    app.run()
