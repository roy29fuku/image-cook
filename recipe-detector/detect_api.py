from flask import Flask, request
import json
import sys, os
from PIL import Image
import numpy as np
import ingre_cnn as ingre

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/', methods=['POST'])
def detect():
    # TODO: ingre_checker.pyを流用したので複数ファイルチェック用になっているので冗長な部分を削減したい
    request_json = json.loads(request.data)

    # fname = 'images/test-tomato.jpg'
    image_size = 50

    X = []
    # files = []
    categories = [
        'carrot',
        'onion',
        'radish',
        'tomato',
        'cabbage',
    ]

    # img = Image.open(fname)
    # img = img.convert("RGB")
    # img = img.resize((image_size, image_size))
    in_data = np.asarray(request_json)

    X.append(in_data)
    # files.append(fname)
    X = np.array(X)

    model = ingre.build_model(X.shape[1:])
    model.load_weights("./models/ingredient-cnn-model.hdf5")

    pre = model.predict(X)

    for i, p in enumerate(pre):
        y = p.argmax()
        print("| 食材名:", categories[y])

    return 'hoge'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
