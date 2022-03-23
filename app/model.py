from app import db
import enum
from sqlalchemy import Enum, Integer

class PropertyType(enum.Enum):
    house = 'House'
    apartment = 'Apartment'
    


class PropertyModel(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    numberofbdr = db.Column(db.Integer)
    numberofbath = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.Numeric(10,2))
    property_type = db.Column(Enum(PropertyType))
    description = db.Column(db.String(300))
    photo = db.Column(db.String(300))
    


    def __init__(self, title, numberofbdr, numberofbath, location, price, property_type, description, photo):

        self.title = title
        self.numberofbdr = numberofbdr
        self.numberofbath = numberofbath
        self.location = location
        self.price = price
        self.property_type = property_type
        self.description = description
        self.photo = photo