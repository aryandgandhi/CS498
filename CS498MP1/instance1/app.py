from flask import Flask, request, jsonify

app = Flask(__name__)


seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():

    return str(seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value
    seed_value = request.json["num"]
    return "OK", 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
