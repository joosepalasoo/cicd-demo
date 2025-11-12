from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'CI/CD Demo API',
        'version': '1.0.0',
        'timestamp': str(datetime.now())
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

@app.route('/products')
def products():
    return jsonify([
        {'id': 1, 'name': 'Laptop', 'price': 999},
        {'id': 2, 'name': 'Phone', 'price': 599}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
