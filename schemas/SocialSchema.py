from marshmallow import Schema, fields

class SocialSchema(Schema):
    Id = fields.Int(dump_only=True)  # Solo para la salida, no para la entrada
    UserId = fields.Int(required=True)
    Platform = fields.Str(required=True)
    Link = fields.Str(required=True)
    Risk = fields.Int(required=True)
