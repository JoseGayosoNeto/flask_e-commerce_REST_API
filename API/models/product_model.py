from API import db

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer,primary_key = True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    regular_price = db.Column(db.DECIMAL, nullable=False)

    def __repr__(self):
        return f"Product('{self.id}', '{self.product_name}', '{self.description}', '{self.quantity}','{self.regular_price}')"