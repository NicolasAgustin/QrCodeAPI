import jwt

from decouple import config
from flask import Flask, jsonify, request
from modules.Mongo import Mongo
from modules.auth_middleware import token_required
from modules.qr_generator import generate_qr, decode_qr


app = Flask(__name__)

app.config['SECRET_KEY'] = config('SECRET_KEY')

DATABASE = Mongo(
    config('DB_PORT'),
    config('DB_IP'),
    config('DB_NAME')
)


@app.route('/encode/<text>', methods=['GET'])
@token_required
def encode(text: str):
    return generate_qr(text)


@app.route('/decode', methods=['POST'])
@token_required
def decode():
    return decode_qr(request.data)


@app.route('/auth', methods=['POST'])
def auth():
    try:
        data = request.json
        if not data:
            return {
                'message': 'Please provide credentials',
                'data': None,
                'error': 'Bad request'
            }, 400

        validated = DATABASE.get_user_by_pass_email(
            data.get('password'),
            data.get('user')
        )

        if not validated:
            return jsonify({
                'message': 'Invalid credentials',
                'data': None,
                'error': validated
            }), 400

        token = jwt.encode(
            {
                'user': validated['user'],
                'password': validated['password']
            },
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )

        return jsonify({
            'message': 'Successfully fetched auth token',
            'data': token
        }), 200

    except Exception as e:
        return jsonify({
            "message": "Something went wrong!",
            "error": str(e),
            "data": None
        }), 500


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    return jsonify({
        'code': 200,
        'description': str(e)
    })


if __name__ == '__main__':
    app.run()
