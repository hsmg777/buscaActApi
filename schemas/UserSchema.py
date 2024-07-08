from marshmallow import Schema, fields

class UserSchema(Schema):
    id_user = fields.Int(dump_only=True)  
    name = fields.Str(required=True)
    password = fields.Str(required=True)
