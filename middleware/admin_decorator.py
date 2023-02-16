from functools import wraps
from flask import request, jsonify
import jwt


def admin_required(f):

    # '@wraps' decorator'ü, bir iç fonksiyonu sarmalayan bir fonksiyon decorator'üdür. Bu, sarmalanan fonksiyonun
    # özelliklerini koruyarak bir fonksiyonu dekore etmenize olanak tanır. Bir fonksiyon decorator'ü,
    # bir iç fonksiyon tanımlar ve bu iç fonksiyon, sarmalanacak olan orijinal fonksiyonun işlevselliğini genişletir
    # veya değiştirir. Ancak, bu sarmalama işlemi orijinal fonksiyonun meta verileri (docstring, isim,
    # imza vb.) kaybolabilir. Bu nedenle, @wraps(f) kullanarak, iç fonksiyonu, sarmalanan fonksiyonun meta
    # verileriyle birlikte sarmalayarak, sarmalanan fonksiyonun özelliklerini korur.

    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return jsonify({'message': 'Authorization header is missing'}), 401
        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            if payload['role'] != 'admin':
                return jsonify({'message': 'Unauthorized access, admin role required'}), 401
        except jwt.exceptions.InvalidSignatureError:
            return jsonify({'message': 'Invalid token signature'}), 401
        except jwt.exceptions.DecodeError:
            return jsonify({'message': 'Invalid token format'}), 401

        return f(*args, **kwargs)

    return decorated_function
