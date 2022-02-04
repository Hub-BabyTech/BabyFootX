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
    d['Balls'] = [[10,10],[20,30],[50,50],[40,77],[23,45]]
    return jsonify(d) 

if __name__ == '__main__':
    # t = threading.Thread(target=babyFoot)
    # t.start()
    app.run()


# chrome://inspect/#devices