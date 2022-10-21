from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/<string:employee>', methods = ['POST'])
def disp(employee):
    data = "Hello"
    return jsonify({'data': data + " "+ employee})

if __name__ == '__main__':
	app.run(debug = True)