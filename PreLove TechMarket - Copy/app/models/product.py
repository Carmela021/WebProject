from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id        = db.Column(db.Integer, primary_key=True)
    name      = db.Column(db.String(150), nullable=False)
    desc      = db.Column(db.String(300))
    price     = db.Column(db.Float, nullable=False)
    old_price = db.Column(db.Float, nullable=True)
    condition = db.Column(db.String(20))
    image     = db.Column(db.String(300))
    tag       = db.Column(db.String(50))
    category  = db.Column(db.String(50))

    def __repr__(self):
        return f'<Product {self.name}>'