from flask import Flask
from serverless_wsgi import handle_request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/home')
def hello():
    return 'Welcome to home!'
def lambda_handler(event, context):
    return handle_request(app, event, context)