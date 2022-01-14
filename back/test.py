#!/usr/bin/env python3

import sys
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/api")
def hello():
    d = {}
    d['Query'] = str(request.args['Query'])
    # res = jsonify(d['Query'])
    # res = "Hello flutter, this text come from python3 and your text : " + d
    return jsonify(d)

@app.route("/")
def test():
    return "oui"

if __name__ == "__main__":
    app.run()