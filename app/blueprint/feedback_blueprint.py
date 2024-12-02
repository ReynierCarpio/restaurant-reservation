from flask_smorest import Blueprint
from flask import abort
from app.repository.feedback_repository import FeedbackRepository
from app.schema.feedback_schema import FeedbackSchema

feedback_blp = Blueprint('feedback', 'feedback', url_prefix='/feedback', description="Operations for feedback")

@feedback_blp.route("/", methods=['POST'])
@feedback_blp.arguments(FeedbackSchema)
@feedback_blp.response(201, FeedbackSchema)
def create_feedback(data):
    return FeedbackRepository.create_feedback(data)

@feedback_blp.route("/<uuid:feedback_uuid>", methods=['GET'])
@feedback_blp.response(200, FeedbackSchema)
def get_feedback_by_uuid(feedback_uuid):
    feedback = FeedbackRepository.get_feedback_by_uuid(str(feedback_uuid))
    if not feedback:
        abort(404, description="Feedback not found")
    return feedback

@feedback_blp.route("/", methods=['GET'])
@feedback_blp.response(200, FeedbackSchema(many=True))
def get_all_feedback():
    return FeedbackRepository.get_all()

@feedback_blp.route("/<uuid:feedback_uuid>", methods=['PUT'])
@feedback_blp.arguments(FeedbackSchema)
@feedback_blp.response(200, FeedbackSchema)
def update_feedback(data, feedback_uuid):
    feedback = FeedbackRepository.get_feedback_by_uuid(str(feedback_uuid))
    if not feedback:
        abort(404, description="Feedback not found")
    return FeedbackRepository.update_feedback(feedback, data)

@feedback_blp.route("/<uuid:feedback_uuid>", methods=["DELETE"])
@feedback_blp.response(204)
def delete_feedback(feedback_uuid):
    feedback = FeedbackRepository.get_feedback_by_uuid(str(feedback_uuid))
    if not feedback:
        abort(404, description="Feedback not found")
    FeedbackRepository.delete_feedback(feedback)
    return ''
