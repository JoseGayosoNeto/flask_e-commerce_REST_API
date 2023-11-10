from API import db
class Cart(db.Model):
    __tablename__ = "cart"
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True,nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    
    def __repr__(self,product_id,quantity,user_id):
        return f"Item('{self.product_id}', '{self.quantity}', User_id: '{self.user_id}')"