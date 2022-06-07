from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'sgeTestOne (main Tue Jun  7 16:28:36 PDT 2022) says Hello, Docker!'
