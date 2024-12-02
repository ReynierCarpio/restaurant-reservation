from flask_smorest import Blueprint
from flask import abort
from app.repository.user_info_repository import UserInfoRepository
from app.schema.user_info_schema import UserInfoSchema

user_info_blp = Blueprint('user_info', 'user_info', url_prefix='/user-info', description="Operations for user info")

@user_info_blp.route("/", methods=['POST'])
@user_info_blp.arguments(UserInfoSchema)
@user_info_blp.response(201, UserInfoSchema)
def create_user_info(data):
    return UserInfoRepository.create_user_info(data)

@user_info_blp.route("/<uuid:user_info_uuid>", methods=['GET'])
@user_info_blp.response(200, UserInfoSchema)
def get_user_info_by_uuid(user_info_uuid):
    user_info = UserInfoRepository.get_user_info_by_uuid(str(user_info_uuid))
    if not user_info:
        abort(404, description="User info not found")
    return user_info

@user_info_blp.route("/", methods=['GET'])
@user_info_blp.response(200, UserInfoSchema(many=True))
def get_all_user_info():
    return UserInfoRepository.get_all()

@user_info_blp.route("/<uuid:user_info_uuid>", methods=['PUT'])
@user_info_blp.arguments(UserInfoSchema)
@user_info_blp.response(200, UserInfoSchema)
def update_user_info(data, user_info_uuid):
    user_info = UserInfoRepository.get_user_info_by_uuid(str(user_info_uuid))
    if not user_info:
        abort(404, description="User info not found")
    return UserInfoRepository.update_user_info(user_info, data)

@user_info_blp.route("/<uuid:user_info_uuid>", methods=["DELETE"])
@user_info_blp.response(204)
def delete_user_info(user_info_uuid):
    user_info = UserInfoRepository.get_user_info_by_uuid(str(user_info_uuid))
    if not user_info:
        abort(404, description="User info not found")
    UserInfoRepository.delete_user_info(user_info)
    return ''
