from flask import Flask, request, jsonify

app = Flask(__name__)


seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():

    return jsonify(seed=seed_value)

@app.route('/', methods=['POST'])
def update_seed():
    global seed_value

    request_data = request.get_json()
    seed_value = request_data.get('num', seed_value)
    return jsonify(message="Seed value updated", new_seed=seed_value), 200

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
