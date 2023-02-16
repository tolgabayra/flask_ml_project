from flask import Blueprint, jsonify, request, make_response
from service.auth_service import AuthService


auth_controller = Blueprint('auth_controller', __name__)


@auth_controller.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']

    access_token = AuthService.login(email, password)
    if access_token is None:
        return jsonify({"message": "Invalid email or password"}), 401

    response = jsonify({"access_token": access_token})
    response.set_cookie('access_token', access_token, httponly=True)
    return response, 200


@auth_controller.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([name, email, password]):
        return jsonify({'message': 'Missing required parameters'}), 400

    user = AuthService.register(name, email, password)
    return jsonify({'message': 'User registered successfully', 'user': user.to_dict()}), 201
