from flask import Flask, request, jsonify


app = Flask(__name__)


seed_value = 0

@app.route('/', methods=['GET'])
def get_seed():
    import socket
    return socket.gethostname()

@app.route('/', methods=['POST'])
def update_seed():
    
   



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
