from db import db

class BusquedaSubdominios(db.Model):
    __tablename__ = 'BusquedaSubdominios'
    Id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.Integer, nullable=False)  # Ajusta el tipo de dato según tu esquema de usuarios
    Subdomain = db.Column(db.String(255), nullable=False)
    IP = db.Column(db.String(50))
    SubdomainRisk = db.Column(db.Integer)
    IPRisk = db.Column(db.Integer)
    FechaHora = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __init__(self, UserId, Subdomain, IP=None, SubdomainRisk=None, IPRisk=None):
        self.UserId = UserId
        self.Subdomain = Subdomain
        self.IP = IP
        self.SubdomainRisk = SubdomainRisk
        self.IPRisk = IPRisk
