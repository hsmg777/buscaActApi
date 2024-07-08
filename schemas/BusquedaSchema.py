from marshmallow import Schema, fields

class BusquedaSchema(Schema):
    Id = fields.Int(dump_only=True)
    UserId = fields.Int(required=True)
    Subdomain = fields.Str(required=True)
    IP = fields.Str()
    SubdomainRisk = fields.Int()
    IPRisk = fields.Int()
    FechaHora = fields.DateTime(dump_only=True)
