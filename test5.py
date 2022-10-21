from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def disp():
    print("enter Marks in English")
    English = input()
    print("enter Marks in Maths")
    Maths = input()
    Total = int(English) + int(Maths)
    print(Total)
    return jsonify({'Total = ': Total})

if __name__ == '__main__':
	app.run(debug = True)