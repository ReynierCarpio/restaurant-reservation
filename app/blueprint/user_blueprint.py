# app/blueprint/user_blueprint.py
from flask_smorest import Blueprint
from flask import abort
from app.repository.user_repository import UserRepository
from app.schema.user_schema import UserSchema

# Correctly initialize the blueprint with 'user_blueprint' as the name
user_blueprint = Blueprint('users', __name__, url_prefix='/users', description="Operations for users")

@user_blueprint.route("/", methods=['POST'])
@user_blueprint.arguments(UserSchema)
@user_blueprint.response(201, UserSchema)
def create_user(data):
    user = UserRepository.create_user(data)
    return user

@user_blueprint.route("/<uuid:user_uuid>", methods=['GET'])
@user_blueprint.response(200, UserSchema)
def get_user_by_uuid(user_uuid):
    user = UserRepository.get_user_by_uuid(str(user_uuid))  # Convert UUID to string for querying
    if not user:
        abort(404, description="User not found")
    return user

@user_blueprint.route("/", methods=['GET'])
@user_blueprint.response(200, UserSchema(many=True))
def get_all_users():
    return UserRepository.get_all()

@user_blueprint.route("/<uuid:user_uuid>", methods=['PUT'])
@user_blueprint.arguments(UserSchema)
@user_blueprint.response(200, UserSchema)
def update_user(data, user_uuid):
    user = UserRepository.get_user_by_uuid(str(user_uuid))
    if not user:
        abort(404, description="User not found")
    return UserRepository.update_user(user, data)

@user_blueprint.route("/<uuid:user_uuid>", methods=["DELETE"])
@user_blueprint.response(204)
def delete_user(user_uuid):
    user = UserRepository.get_user_by_uuid(str(user_uuid))
    if not user:
        abort(404, description="User not found")
    UserRepository.delete_user(user)
    return ''
