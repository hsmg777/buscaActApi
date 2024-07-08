from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.BusquedaSubdominios import BusquedaSubdominios
from db import db
from schemas.BusquedaSchema import BusquedaSchema
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint(
    "BusquedaSubdominios",
    "subdo",
    url_prefix="/api/subdo",
    description="CRUD for subdo"
)

# Instancia del esquema
subdo_schema = BusquedaSchema()
subdos_schema = BusquedaSchema(many=True)
# GET /api/contact
@blp.route('/')
class SubdoList(MethodView):
    @blp.response(200, BusquedaSchema)
    def get(self):
        subdos = BusquedaSubdominios.query.all()
        print(subdos)  # Verifica qué se está devolviendo aquí
        return subdos

    @blp.arguments(BusquedaSchema)  # Define el esquema para la carga útil
    @blp.response(201, BusquedaSchema)  # Define el esquema para la respuesta
    
    def post(self, data):
        nuevo_user = BusquedaSubdominios(
            UserId=data['UserId'],
            Subdomain=data['Subdomain'],
             IP=data['IP'],
             SubdomainRisk=data['SubdomainRisk'],
             IPRisk=data['IPRisk']
            )
           
        db.session.add(nuevo_user)
        db.session.commit()
        return nuevo_user

# GET, PUT, DELETE /api/contact/<int:idContact>
@blp.route('/<int:Id>')
class SubdoResource(MethodView):
    @blp.response(200, BusquedaSchema)  # Define el esquema para la respuesta
    def get(self, Id):
        user = BusquedaSubdominios.query.get(Id)
        if user is None:
            abort(404, message="Contact no encontrado")
        return user
    @blp.arguments(BusquedaSchema)  # Define el esquema para la carga útil
    @blp.response(200, BusquedaSchema)  # Define el esquema para la respuesta
    def put(self, data, Id):
        user = BusquedaSubdominios.query.get(Id)
        if user is None:
            abort(404, message="Contact no encontrado")
        
        user.UserId=data['UserId']
        user.Subdomain=data['Subdomain']
        user.IP=data['IP']
        user.SubdomainRisk=data['SubdomainRisk']
        user.IPRisk=data['IPRisk']
        
        db.session.commit()
        return user

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, Id):
        user = BusquedaSubdominios.query.get(Id)
        if user is None:
            abort(404, message="Contact no encontrado")
        db.session.delete(user)
        db.session.commit()
        return '', 204
    
@blp.route('/user/<int:UserId>')
class GetAllUserId(MethodView):
    @blp.response(200, subdos_schema)  # Define el esquema para la respuesta
    def get(self, UserId):
        subdos = BusquedaSubdominios.query.filter_by(UserId=UserId).all()
        if not subdos:
            abort(404, message=f"No se encontraron subdominios para UserId {UserId}")
        return subdos
