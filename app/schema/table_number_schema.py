from marshmallow import Schema, fields

class TableNumberSchema(Schema):
    table_id = fields.Int(dump_only=True)
    table_uuid = fields.Str(dump_only=True)
    table_number = fields.Str(required=True)
    restaurant_id = fields.Int(required=True)
    status = fields.Str(required=True, validate=lambda x: x in ['Available', 'Reserved', 'Occupied'])
    seat = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(dump_only=True)
