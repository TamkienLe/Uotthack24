from flask import Flask
from flask import request
from google.cloud import vision
import constants
import stringAlgs.text_extract as text_extract

client = vision.ImageAnnotatorClient()

app = Flask(__name__)
client = vision.Client()

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/visionText', methods=['POST'])
def visionText():
    print(f'request: {request}')
    return f'hello {request.form}'
