from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.SocialMediaLinks import SocialMediaLink
from db import db
from schemas.SocialSchema import SocialSchema
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint(
    "SocialMediaLinks",
    "social",
    url_prefix="/api/social",
    description="CRUD for social"
)

# Instancia del esquema
social_schema = SocialSchema()
social_schema = SocialSchema(many=True)
# GET /api/contact
@blp.route('/')
class SocialList(MethodView):
    @blp.response(200, SocialSchema)
    def get(self):
        subdos = SocialMediaLink.query.all()
        print(subdos)  # Verifica qué se está devolviendo aquí
        return subdos

    @blp.arguments(SocialSchema)  # Define el esquema para la carga útil
    @blp.response(201, SocialSchema)  # Define el esquema para la respuesta
    
    def post(self, data):
        nuevo_user = SocialMediaLink(
            UserId=data['UserId'],
            Platform=data['Platform'],
             Link=data['Link'],
             Risk=data['Risk']
            )
           
        db.session.add(nuevo_user)
        db.session.commit()
        return nuevo_user

# GET, PUT, DELETE /api/contact/<int:idContact>
@blp.route('/<int:Id>')
class SubdoResource(MethodView):
    @blp.response(200, SocialSchema)  # Define el esquema para la respuesta
    def get(self, Id):
        user = SocialMediaLink.query.get(Id)
        if user is None:
            abort(404, message="Contact no encontrado")
        return user
    @blp.arguments(SocialSchema)  # Define el esquema para la carga útil
    @blp.response(200, SocialSchema)  # Define el esquema para la respuesta
    def put(self, data, Id):
        user = SocialMediaLink.query.get(Id)
        if user is None:
            abort(404, message="Contact no encontrado")
        
        user.UserId=data['UserId']
        user.Platform=data['Platform']
        user.Link=data['Link']
        user.Risk=data['Risk']
        
        db.session.commit()
        return user

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, Id):
        user = SocialMediaLink.query.get(Id)
        if user is None:
            abort(404, message="Contact no encontrado")
        db.session.delete(user)
        db.session.commit()
        return '', 204
    
@blp.route('/user/<int:UserId>')
class GetAllUserId(MethodView):
    @blp.response(200, social_schema)  # Define el esquema para la respuesta
    def get(self, UserId):
        subdos = SocialMediaLink.query.filter_by(UserId=UserId).all()
        if not subdos:
            abort(404, message=f"No se encontraron subdominios para UserId {UserId}")
        return subdos
