from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'sgeTestOne (my-new-feature-branch) says Hello, Docker!'
