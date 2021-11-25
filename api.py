import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  data = list(reader)

my_data = [
    {
        'Name' : 'Amrita',
        'Class' : 'IX',
        'Serial_number' : '07'
    },
    {
        'Hobby' : 'Drawing',
        'Favorite_color' : 'Red, purple',
        'Address' : 'Netaji Pally, Sainthia, Birbhum'
    }
]
@app.route("/")
def my_first_api():
    return "My first API"

@app.route("/my_first_api_data")
def my_first_api_1():
    return "12345"

@app.route("/my_data")
def my_first_api_2():
    return jsonify({
        "data": my_data,
        "message": "success"
    }), 200

    
@app.route("/api_input", methods = ["POST"])
def my_first_api_3():
    new_data = [{
        '1' : 'a',
    }]
    my_data.append(new_data)
    
    return jsonify({
        "data": my_data,
        "message": "success"
    }), 200
      

if __name__ == "__main__":
    app.run()

