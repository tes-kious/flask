from flask import Flask, jsonify, request
import os
import mongoservices

app = Flask(__name__)
mongosvc = mongoservices.mongoservices()

@app.route('/')
def index():
    return jsonify({"Hallo": "Welcome to your Flask Application"})

@app.route('/api/menu')
def menu():
    return jsonify({"code": "1", "status": "OK", "menus":"menus"})

@app.route('/api/samples', methods=['POST'])
def save_sample():
    data = request.json
    return mongosvc.save_sample(data)
    
@app.route('/api/findDriver', methods=['POST'])
def select_sample():
    data = request.json
    return mongosvc.select_driver(data)

@app.route('/api/find', methods=['POST'])
def select_sample():
    data = request.json
    return mongosvc.select_sample(data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
