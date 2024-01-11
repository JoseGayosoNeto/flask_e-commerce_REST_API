from ..services import transaction_service, transactionItem_service
from ..schemas import transaction_schema, transactionItemPurchase_schema
from ..models.transaction_model import Transaction
from API import api
from flask import make_response,jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..decorator import admin_required
from ..paginate import paginate
from ..models.enumerate import TransactionType

class TransactionList(Resource):
    
    @admin_required
    def get(self):
        ts = transaction_schema.TransactionSchema(many=True)
        return paginate(Transaction, ts)

class TransactionDetails(Resource):
    
    @jwt_required()
    def get(self,transaction_id):
        
        claims = get_jwt()
        user_id = claims['user_id']
        
        is_logged_user_transaction = transaction_service.is_logged_user_transaction(user_id=user_id,transaction_id=transaction_id)
        if is_logged_user_transaction == False:
            return make_response(jsonify("Transaction not found."), 404)
        transaction_items = transactionItem_service.list_transaction_by_id(transaction_id)
        transaction = transaction_service.list_transaction_by_transaction_id(transaction_id)
        if transaction.transaction_type == TransactionType.BALANCE:
            ts = transaction_schema.TransactionSchema()
            return make_response(ts.jsonify(transaction), 200)
        else:
            tis = transactionItemPurchase_schema.TransactionItemPurchaseSchema(many=True)
            return make_response(tis.jsonify(transaction_items), 200)
        
        

api.add_resource(TransactionList, '/transactions')
api.add_resource(TransactionDetails, '/transactions/transaction/<int:transaction_id>/details')
            