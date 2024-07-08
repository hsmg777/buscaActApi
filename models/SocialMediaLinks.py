from db import db

class SocialMediaLink(db.Model):
    __tablename__ = 'SocialMediaLinks'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserId = db.Column(db.Integer, nullable=False)
    Platform = db.Column(db.String(50), nullable=False)
    Link = db.Column(db.String, nullable=False)
    Risk = db.Column(db.Integer, nullable=False)
    
    def __init__(self, UserId, Platform, Link, Risk):
        self.UserId = UserId
        self.Platform = Platform
        self.Link = Link
        self.Risk = Risk
