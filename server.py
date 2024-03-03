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
    print("test")


    # GUNK START

    # print("form: ", request.form)
    b64image = request.form['files']
    print('base64 content: ', b64image)

    content = base64.b64decode(b64image)

    print('bytes content: ', content)
    
    # print("Full Path:", request.full_path)
    # print("URL:", request.url)
    # print("Method:", request.method)
    # print("Headers:\n", request.headers)




    # print(request.get_data(as_text=True, parse_form_data=True, cache=False))


    # GUNK END

    # request.data
    # content = request.files['image'].read()

    image = vision.Image(content=content)

    # Use cloud vision to get text
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # 1st description from cloud vision looks like it's all of the text found
    item_data = text_extract.extract_content(texts[0].description)

    print(item_data)

    algo.algo(item_data)

    # print(f"Your brand's ethical manufacturing practice is rated {algo.brand_score}/100")
    pass

    # Create response for client

    return item_data
