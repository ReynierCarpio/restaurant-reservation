from marshmallow import Schema, fields

class ReservationSchema(Schema):
    reservation_id = fields.Int(dump_only=True)
    reservation_uuid = fields.Str(dump_only=True)
    restaurant_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    table_id = fields.Int(required=True)
    reservation_date_time = fields.DateTime(required=True)
    status = fields.Str(required=True, validate=lambda x: x in ['Pending', 'Confirmed', 'Cancelled'])
    guests = fields.Int(required=True)
    special_request = fields.Str(allow_none=True)
    party_size = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
