from flask import request, jsonify, Blueprint
from service.user_service import UserService
from middleware.jwt_required import jwt_required

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


@user_controller.route("users/<int:id>", methods=["PUT"])
def update_user(id):
    result = UserService.update_user(id, request.get_json())
    if result:
        return jsonify("User has been updated."), 200
    else:
        return jsonify("User not found"), 404


@user_controller.route("users", methods=["GET"])
@jwt_required
def list_user():
    records = UserService.list_user()
    return jsonify([records.to_dict() for record in records]), 200


@user_controller.route("users<int:id>", methods=["GET"])
def show_user(id):
    record = UserService.show_user(id)
    if record:
        return jsonify(record.to_dict()), 200
    else:
        return jsonify("user not found"), 404







