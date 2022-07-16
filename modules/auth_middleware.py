import jwt

from flask import jsonify, request
from flask import current_app
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            return {
                'message': 'Authentication token is missing.',
                'data': None,
                'error': 'Unauthorized'
            }, 400
        try:
            data = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256']
            )

            # Hay que chequear el contenido del token
            if data['user'] != 'qrcode1' and data['password'] != 'pass123':
                return jsonify({
                    "message": "Invalid Authentication token!",
                    "data": None,
                    "error": "Unauthorized"
                }), 401

        except Exception as e:
            return {
                'message': 'Something went wrong',
                'data': None,
                'error': str(e)
            }, 500

        return f(*args, **kwargs)

    return decorated
