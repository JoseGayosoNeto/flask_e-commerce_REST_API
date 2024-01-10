from API import db
from ..models import transaction_model


def make_transactionItems_history(transactionItem):
    transaction_item = transaction_model.TransactionItem(transaction_id=transactionItem.transaction_id,product_id=transactionItem.product_id, quantity=transactionItem.quantity, unit_price=transactionItem.unit_price)
    db.session.add(transaction_item)
    db.session.commit()
    return transaction_item

def list_transaction_by_id(id):
    transaction_items = transaction_model.TransactionItem.query.filter_by(transaction_id=id).all()
    return transaction_items