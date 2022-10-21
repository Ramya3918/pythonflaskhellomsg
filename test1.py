from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def home():
    data = "Hello Ramya"
    return jsonify({'data': data})

if __name__ == '__main__':
	app.run(debug = True)