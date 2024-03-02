from google.cloud import vision
import constants

client = vision.ImageAnnotatorClient()

with open('/Users/lukamacieszczak/Downloads/IMG_2358.jpg', "rb") as image_file:
        content = image_file.read()


image = vision.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations

print(texts[0].description.split('\n'))

# CA and RN numbers may appear on the same line

# print("Texts:")

# for text in texts:
#     containsMaterial = False
#     for m in constants.MATERIALS:
#         if m in text.description: containsMaterial = True

#     # if containsMaterial:
#     print(f'\n"{text.description}"')

#     vertices = [
#         f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
#     ]

#     # print("bounds: {}".format(",".join(vertices)))

# if response.error.message:
#     raise Exception(
#         "{}\nFor more info on error messages, check: "
#         "https://cloud.google.com/apis/design/errors".format(response.error.message)
#     )
