from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/<int:num>', methods = ['POST'])
def disp(num):
	return jsonify({'data': num**2})

if __name__ == '__main__':

	app.run(debug = True)
