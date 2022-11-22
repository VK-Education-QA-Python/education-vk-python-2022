#!/usr/bin/env python3

import os
import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/get_age/<name>', methods=['GET'])
def get_user_age(name):
    return jsonify(random.randint(18, 105)), 200


if __name__ == '__main__':
    host = os.environ.get('STUB_HOST', '127.0.0.1')
    port = os.environ.get('STUB_PORT', '4444')

    app.run(host, port)
