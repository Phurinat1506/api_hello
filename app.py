from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Home from Flask on Kubernetes!"

@app.route('/hello')
def hello():
    return "Hello from Flask on Kubernetes!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)