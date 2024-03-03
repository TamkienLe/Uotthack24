from flask import Flask
from flask import request
from google.cloud import vision
import text_extract as text_extract

client = vision.ImageAnnotatorClient()

app = Flask(__name__)

@app.route('/visionText', methods=['POST'])
def visionText():
    content = request.files['image'].read()
    image = vision.Image(content=content)

    # Use cloud vision to get text
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # 1st description from cloud vision looks like it's all of the text found
    item_data = text_extract.extract_content(texts[0].description)

    print(item_data)

    # Do Saad algo to come up  with carbon footprint
    pass

    # Create response for client

    return item_data
