from flask import Flask
from flask import request
from google.cloud import vision

app = Flask(__name__)
client = vision.Client()

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def test():
    return f'hello {request.args}'

@app.route('/testpost', methods=['POST'])
def testpost():
    print(f'request: {request}')
    return f'hello {request.form}'
