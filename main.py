from flask import Flask, jsonify
import gdown
app = Flask(__name__)

@app.route('/run')
def run_colab():
    #gdown.download('https://colab.research.google.com/drive/1TlhVz7CA8L0AC1s3tmZqVOxtiKmyVk6z','GPTTrader.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')


@app.route("/")
def home():
    return "Hello Verceller"


@app.route('/run')
def run_colab():
    gdown.download('https://colab.research.google.com/drive/1TlhVz7CA8L0AC1s3tmZqVOxtiKmyVk6z','GPTTrader.ipynb', quiet=False)
    return jsonify(message='colab notebook ran successfully')
