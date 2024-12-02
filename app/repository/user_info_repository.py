from app.extension import db
from app.models.user_info_model import UserInfoModel

class UserInfoRepository:

    @staticmethod
    def create_user_info(data):
        user_info = UserInfoModel(**data)
        db.session.add(user_info)
        db.session.commit()
        return user_info

    @staticmethod
    def get_user_info_by_uuid(user_info_uuid):
        return UserInfoModel.query.filter_by(user_info_uuid=user_info_uuid, deleted_at=None).first()

    @staticmethod
    def get_all():
        return UserInfoModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_user_info(user_info, data):
        for key, value in data.items():
            setattr(user_info, key, value)
        db.session.commit()
        return user_info

    @staticmethod
    def delete_user_info(user_info):
        user_info.deleted_at = db.func.current_timestamp()
        db.session.commit()
