from API import app, db
from sqlalchemy import Enum
from .enumerate import TransactionType, TransactionStatus

class Transaction(db.Model):
    __tablename__ = "transaction"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    total_amount = db.Column(db.Numeric(10,2), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    transaction_type = db.Column(Enum(TransactionType), nullable=False)
    status = db.Column(Enum(TransactionStatus), nullable=False)
    
    transaction_user = db.relationship("User", backref="transactions")
    transaction_items = db.relationship("TransactionItem", backref="transaction", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Transaction('{self.id}', '{self.user_id}', '{self.total_amount}', '{self.transaction_date}', '{self.transaction_type}')"
    
class TransactionItem(db.Model):
    __tablename__ = 'transaction_item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey("transaction.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    
    products = db.relationship("Product", backref="transactions")
    
    def __repr__(self):
        return f"TransactionItem('{self.id}', '{self.transaction_id}', '{self.product_id}', '{self.quantity}', '{self.unit_price}')"
    
