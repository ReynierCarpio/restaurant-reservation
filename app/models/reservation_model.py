import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql.sqltypes import Enum
from app.extension import db

class ReservationModel(db.Model):
    __tablename__ = "reservation"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservation_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('table_number.table_id'), nullable=False)
    reservation_date_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(Enum('Pending', 'Confirmed', 'Cancelled'), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    special_request = db.Column(db.String(255), nullable=True)
    party_size = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    feedbacks = db.relationship('FeedbackModel', backref='reservation', lazy='dynamic')
    user_info = db.relationship('UserInfoModel', backref='reservation', lazy='dynamic')
