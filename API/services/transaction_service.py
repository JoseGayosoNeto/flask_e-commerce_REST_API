from ..models import transaction_model
from API import db

def make_transaction(transaction):
    transaction_db = transaction_model.Transaction(user_id=transaction.user_id,total_amount=transaction.total_amount,transaction_date=transaction.transaction_date,transaction_type=transaction.transaction_type,status=transaction.status)
    db.session.add(transaction_db)
    db.session.commit()
    return transaction_db

def get_total_amount(user_cart):
    total_amount = 0
    for item in user_cart:
        total_amount += item.total_value
        
    return total_amount

def list_all_transactions():
    return transaction_model.Transaction.query.all()

def list_transactions_by_user_id(id):
    return transaction_model.Transaction.query.filter_by(user_id=id).all()

def update_transaction_status_to_completed(transaction):
    transaction.status = "Completed"
    db.session.commit()

def update_transaction_status_to_cancelled(transaction):
    transaction.status = "Cancelled"
    db.session.commit()
    
def delete_transaction(transaction):
    db.session.delete(transaction)
    db.session.commit()