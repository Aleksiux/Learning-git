from flask import Flask, jsonify, request
from calendar import isleap

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'PUT':
        # some_json = request.get_json()
        # return jsonify({'you sent': some_json})
        return jsonify({'you sent': 'asd'})
    else:
        some_json = request.get_json()
        return jsonify({'GET you sent': some_json})


@app.route("/keliamieji/<int:metai>", methods=['GET'])
def keliamieji(metai):
    if isleap(metai):
        return jsonify({'result': "Keliamieji"})
    else:
        return jsonify({'result': "NE Keliamieji"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
