from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
cors = CORS(app)
@app.route('/', methods = ['POST'])
def disp():
	with open(r"\Users\rpasupulati\Desktop\ne\posts.json") as f:
		data = json.load(f)
	return jsonify({'data': data})

if __name__ == '__main__':
	app.run(debug = True)

