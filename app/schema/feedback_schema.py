from marshmallow import Schema, fields

class FeedbackSchema(Schema):
    feedback_id = fields.Int(dump_only=True)
    feedback_uuid = fields.Str(dump_only=True)
    user_id = fields.Int(required=True)
    reservation_id = fields.Int(required=True)
    rating = fields.Int(required=True)
    comments = fields.Str(allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
