from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def disp():
    print("enter your name")
    employee = input()
    data = "Hello"
    return jsonify({'data': data + " "+ employee})

if __name__ == '__main__':
	app.run(debug = True)