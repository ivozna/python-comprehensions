from flask import Flask

app = Flask(__name__)

@app.route("/bunny")
def hello_world():
    return {'blue': 'iscolor', 'green': 'iscolor', 'dog': 'no', 'cat': 'no'}