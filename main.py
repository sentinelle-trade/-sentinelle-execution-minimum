from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def accueil():
    return {"status": "API en ligne"}, 200

@app.route('/tir', methods=['GET'])
def tirer():
    return {"status": "tir déclenché"}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
