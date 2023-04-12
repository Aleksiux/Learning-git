from flask import Flask, jsonify, request
from calendar import isleap

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        print('test good')
        return jsonify({'send_msg': some_json})
    else:
        return jsonify({'about': 'Hello World'})




if __name__ == '__main__':
    app.run()
