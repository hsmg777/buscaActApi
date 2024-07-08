from db import db

class Users(db.Model):
     __tablename__ = 'Users'
     id_user = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(50), nullable=False)
     password = db.Column(db.String(50), nullable=False)
     
     def __init__(self, name, password):
         self.name = name
         self.password = password
 
 