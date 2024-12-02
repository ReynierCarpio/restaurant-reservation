import uuid
from sqlalchemy.dialects.mysql import CHAR
from app.extension import db

class FeedbackModel(db.Model):
    __tablename__ = "feedback"

    feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    feedback_uuid = db.Column(CHAR(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.reservation_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    deleted_at = db.Column(db.DateTime, nullable=True)
