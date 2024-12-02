from marshmallow import Schema, fields

class RestaurantSchema(Schema):
    restaurant_id = fields.Int(dump_only=True)
    restaurant_uuid = fields.Str(dump_only=True)
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    address = fields.Str(required=True)
    contact_number = fields.Int(required=True)
    business_hours = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
