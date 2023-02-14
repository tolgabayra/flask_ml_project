from flask import request, jsonify, Blueprint
from service.user_service import UserService

user_controller = Blueprint("users", __name__)


@user_controller.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = UserService.create_user(data['name'], data['email'])
    return jsonify(user.__dict__), 201


@user_controller.route("/users/<int:id>/", methods=['DELETE'])
def delete_user(id):
    result = UserService.delete_user(id)
    if result:
        return jsonify("User has been delted."), 200
    else:
        return "User not found", 404


@user_controller.route("/users", methods=['GET'])
def tolga():
    return jsonify("Tolga")
