from flask import Flask
from flask import request
app = Flask(__name__)

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




