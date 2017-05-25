from flask import Flask, request
import json
import numpy as np
import ingre_cnn as ingre

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'

@app.route('/', methods=['POST'])
def detect():
    request_json = json.loads(request.data)

    X = []
    categories = [
        'carrot',
        'onion',
        'radish',
        'tomato',
        'cabbage',
    ]
    results = []

    in_data = np.asarray(request_json)

    X.append(in_data)
    X = np.array(X)

    model = ingre.build_model(X.shape[1:])
    model.load_weights("./models/ingredient-cnn-model.hdf5")

    pre = model.predict(X)

    for i, p in enumerate(pre):
        y = p.argmax()
        results.append(categories[y])

    results_json = json.dumps(results, ensure_ascii=False)

    return results_json

if __name__ == '__main__':
    app.run(host='0.0.0.0')
