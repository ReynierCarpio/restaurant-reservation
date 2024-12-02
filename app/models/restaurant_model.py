import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db

class RestaurantModel(db.Model):
    __tablename__ = "restaurant"

    restaurant_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    restaurant_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.Integer, nullable=False)
    business_hours = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    reservations = db.relationship('ReservationModel', backref='restaurant', lazy='dynamic')
    tables = db.relationship('TableNumberModel', backref='restaurant', lazy='dynamic')
