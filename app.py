from flask import Flask, jsonify, request
from modules.qr_generator import generate_qr, decode_qr


app = Flask(__name__)


@app.route('/encode/<text>', methods=['GET'])
def encode(text: str):
    return generate_qr(text)


@app.route('/decode', methods=['POST'])
def decode():
    return decode_qr(request.data)


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    return jsonify({
        'code': 200,
        'description': str(e)
    })


if __name__ == '__main__':
    app.run()
