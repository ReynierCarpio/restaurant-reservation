import uuid
from sqlalchemy.dialects.mysql import CHAR
from sqlalchemy.sql.sqltypes import Enum
from app.extension import db

class TableNumberModel(db.Model):
    __tablename__ = "table_number"

    table_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    table_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    table_number = db.Column(db.String(50), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.restaurant_id'), nullable=False)
    status = db.Column(Enum('Available', 'Reserved', 'Occupied'), nullable=False)
    seat = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    reservations = db.relationship('ReservationModel', backref='table', lazy='dynamic')
