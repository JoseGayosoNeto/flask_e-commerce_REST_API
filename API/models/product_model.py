from API import db
class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer,primary_key = True, autoincrement=True)
    product_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False) 
    quantity = db.Column(db.Integer,nullable=False)
    unit_price = db.Column(db.Numeric(10,2), nullable=False)
    
    def __repr__(self):
        return f"Product('{self.id}', '{self.product_name}', '{self.description}', '{self.quantity}','{self.unit_price}')"