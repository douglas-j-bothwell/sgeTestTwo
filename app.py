from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'sgeTestOne (my-feature-branch updated) says Hello, Docker!'
