from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name=db.column(db.String)
    price=db.column(db.Float)
    image = db.Column(db.String)
    
    def __repr__(self):
     return f'<Plant {self.name} | Price: {self.price}>'