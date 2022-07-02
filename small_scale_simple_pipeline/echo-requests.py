import requests

result = requests.get("http://34.130.85.46:5000/?msg=HelloWorld!")
print(result.json())

result = requests.get("http://34.130.85.46:5000/",  
                       params = { 'msg': 'Hello from params' })
print(result.json())

result = requests.post("http://34.130.85.46:5000/",  
                        json = { 'msg': 'Hello from data' })
print(result.json())

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import io
import base64

image = open("luna.png", "rb").read()
encoded = base64.b64encode(image)
result = requests.get("http:/34.130.85.46:5000/", 
                       json = {'msg': encoded})
encoded = result.json()['response']
imgData = base64.b64decode(encoded)
plt.imshow( np.array(Image.open(io.BytesIO(imgData))))
