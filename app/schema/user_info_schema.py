from marshmallow import Schema, fields

class UserInfoSchema(Schema):
    user_info_id = fields.Int(dump_only=True)
    user_info_uuid = fields.Str(dump_only=True)
    user_id = fields.Int(required=True)
    reservation_id = fields.Str(required=True)
    reference_no = fields.Str(required=True)
    mode_of_payment = fields.Str(required=True, validate=lambda x: x in ['Cash', 'Card', 'Online'])
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
