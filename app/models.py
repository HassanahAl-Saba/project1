from . import db 

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    bedroom = db.Column(db.String(255))
    bathroom = db.Column(db.String(255))    
    location = db.Column(db.String(255))
    price = db.Column(db.String(255))
    type = db.Column(db.String(20))
    description = db.Column(db.String(1080))
    photo = db.Column(db.String(255))

    def __init__(self, title, bedroom, bathroom, location, price, property_type, description, photo):
        self.title = title
        self.bedroom = bedroom
        self.bathroom = bathroom
        self.location = location
        self.price = price  
        self.type = type  
        self.description = description
        self.photo = photo    
