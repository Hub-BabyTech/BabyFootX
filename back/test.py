#!/usr/bin/env python3

import sys
from flask import Flask, request, jsonify
app = Flask(__name__)

# @app.route("/api")
# def hello():
#     d = {}
#     d['Query'] = str(request.args['Query'])
#     # res = jsonify(d['Query'])
#     # res = "Hello flutter, this text come from python3 and your text : " + d
#     return jsonify(d)

# @app.route("/")
# def test():
#     return "oui"

@app.route('/', methods=['GET'])
def index():
    return jsonify([{'id':'0','image':'Hi! this is python'},{'id':'1','image':'that is a test'}])
    # return jsonify({{'id':'0','name':'test'},{'id':'1','name':'hugo'}})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=50162)