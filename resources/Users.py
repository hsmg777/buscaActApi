# Archivo: resources/COntact.py
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models.Users import Users
from db import db
from schemas.UserSchema import UserSchema  # Importa el esquema desde schemas/AboutSchema.py
from marshmallow import ValidationError

# Define el Blueprint
blp = Blueprint("Users", __name__, url_prefix="/api/contact", description="CRUD for user")

# Instancia del esquema
user_schema = UserSchema()
user_schema = UserSchema(many=True)

# GET /api/contact
@blp.route('/')
class UsersList(MethodView):
    @blp.response(200, user_schema)  # Usar contacts_schema para la respuesta de muchos contactos
    def get(self):
        users = Users.query.all()
        return users

    @blp.arguments(UserSchema)  # Define el esquema para la carga útil
    @blp.response(201, UserSchema)  # Define el esquema para la respuesta
    def post(self, data):
        nuevo_user = Users(
            name=data['name'],
            password=data['password'])
        db.session.add(nuevo_user)
        db.session.commit()
        return nuevo_user

# GET, PUT, DELETE /api/contact/<int:idContact>
@blp.route('/<int:id_user>')
class UsersResource(MethodView):
    @blp.response(200, UserSchema)  # Define el esquema para la respuesta
    def get(self, id_user):
        user = UserSchema.query.get(id_user)
        if user is None:
            abort(404, message="Contact no encontrado")
        return user
    @blp.arguments(UserSchema)  # Define el esquema para la carga útil
    @blp.response(200, UserSchema)  # Define el esquema para la respuesta
    def put(self, data, id_user):
        user = Users.query.get(id_user)
        if user is None:
            abort(404, message="Contact no encontrado")
        
        user.name= data['name']
        user.password=data['password']
        
        db.session.commit()
        return user

    @blp.response(204)  # Define el esquema para la respuesta
    def delete(self, id_user):
        user = Users.query.get(id_user)
        if user is None:
            abort(404, message="Contact no encontrado")
        db.session.delete(user)
        db.session.commit()
        return '', 204

