from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

import math

app = Flask(__name__)
CORS(app)
@app.route('/<int:num1>', methods = ['POST'])
def disp(num1):
    print(num1)
    square = math.sqrt(num1)
    print(square)
    return jsonify({'squareroot_of_a_number' :square})
if __name__ == '__main__':
	app.run(debug = True)