#!/usr/bin/python3
from flask import Flask, request, jsonify

# from video import babyFoot
# import os
# import time
# import sys
import threading

from video import getScore, babyFoot

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def hello_world():
    d = {}
    d['Score'] = str("2 - 3")
    d['Red'] = str("34%")
    d['Blue'] = str("66%")
    d['Ball'] = [[10,10],[40,40],[75,75]]
    return jsonify(d) 

if __name__ == '__main__':
    # t = threading.Thread(target=babyFoot)
    # t.start()
    app.run()


# chrome://inspect/#devices