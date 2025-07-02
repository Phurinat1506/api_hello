from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Home from Flask on Kubernetes!"

@app.route('/hello')
def hello():
    return "Hello from Flask on Kubernetes!"

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)