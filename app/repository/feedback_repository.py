from app.extension import db
from app.models.feedback_model import FeedbackModel

class FeedbackRepository:

    @staticmethod
    def create_feedback(data):
        feedback = FeedbackModel(**data)
        db.session.add(feedback)
        db.session.commit()
        return feedback


    @staticmethod
    def get_feedback_by_uuid(feedback_uuid):
        return FeedbackModel.query.filter_by(feedback_uuid=feedback_uuid, deleted_at=None).first()


    @staticmethod
    def get_all():
        return FeedbackModel.query.filter_by(deleted_at=None).all()

    @staticmethod
    def update_feedback(feedback, data):
        for key, value in data.items():
            setattr(feedback, key, value)
        db.session.commit()
        return feedback

    @staticmethod
    def delete_feedback(feedback):
        feedback.deleted_at = db.func.current_timestamp()
        db.session.commit()
