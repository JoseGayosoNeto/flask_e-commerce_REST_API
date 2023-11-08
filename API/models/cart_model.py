from API import db
from ..models.product_model import Product

class Cart(db.Model):
    __tablename__ = "cart"
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self,product_id,quantity):
        return f"Item('{self.product_id}', '{self.quantity}')"