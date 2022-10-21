from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/<int:num1>,<int:num2>', methods = ['POST'])
def disp(num1,num2):
    num3 = num1+num2
    return jsonify({'sum =' :num3})
if __name__ == '__main__':
	app.run(debug = True)