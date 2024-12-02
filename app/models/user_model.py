import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db

class UserModel(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone_number = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    restaurants = db.relationship('RestaurantModel', backref='owner', lazy='dynamic')
    reservations = db.relationship('ReservationModel', backref='user', lazy='dynamic')
    feedbacks = db.relationship('FeedbackModel', backref='user', lazy='dynamic')
    user_info = db.relationship('UserInfoModel', backref='user', lazy='dynamic')
