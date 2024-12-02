import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql.sqltypes import Enum
from app.extension import db

class UserInfoModel(db.Model):
    __tablename__ = "user_info"

    user_info_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_info_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.reservation_id'), nullable=False)
    reference_no = db.Column(db.String(255), nullable=False)
    mode_of_payment = db.Column(Enum('Cash', 'Card', 'Online'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
