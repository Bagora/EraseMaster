from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hello from Flask!'})

def handler(event, context):
    return app.run(port=int(os.environ.get("PORT", 5000)))
