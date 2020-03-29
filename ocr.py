import cv2
import numpy as np
import requests
import io
import json

img = cv2.imread("image.jpg")
height, width, _ = img.shape

#cutting image
roi = img#[290: 550, 100: 850]
cv2.imshow("roi", roi)

#ocr
url_api = "https://api.ocr.space/parse/image"
_, compressedimage = cv2.imencode(".jpg", roi, [1, 90])
file_bytes = io.BytesIO(compressedimage)

result = requests.post(url_api, files = {"image.jpg": file_bytes}, data = {"apikey": "xxxxxxxxxxxxxxx"})

result = result.content.decode()
result = json.loads(result)

text_detected = result.get("ParsedResults")[0].get("ParsedText")
print(text_detected)

#cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows