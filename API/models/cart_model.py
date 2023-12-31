from API import db 
class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False, )
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_value = db.Column(db.Numeric(10,2), nullable=False)
    cart_user = db.relationship("User", back_populates="cart")
    product = db.relationship("Product", backref="carts")

    def __repr__(self):
        return f"Item('{self.product_id}', '{self.quantity}', Total Value: '{self.total_value}', User_id: '{self.user_id}')"

from ..models import user_model