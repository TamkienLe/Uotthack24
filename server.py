from flask import Flask
from flask import request
from google.cloud import vision
import text_extract as text_extract
import algo
import jsonify
import base64

client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/visionText', methods=['POST'])
def visionText():

    b64image = request.form['files']
    content = base64.b64decode(b64image)

    image = vision.Image(content=content)

    # Use cloud vision to get text
    response = client.text_detection(image=image)

    texts = response.text_annotations

    # 1st description from cloud vision looks like it's all of the text found
    print("all text", texts[0].description)
    item_data = text_extract.extract_content(texts[0].description)

    print(item_data)

    #if not item_data or not 'location' in item_data or not item_data.location: return "cant find shit"

    print(item_data)

    test = algo.algo(item_data)

    print(f"Material Footprint: {test[0]}, Shipping Footprint: {test[1]}, Water Usage: {test[2]}, Brand Score: {test[3]}, Final Score: {test[4]}")

    # Create response for client

    return item_data
