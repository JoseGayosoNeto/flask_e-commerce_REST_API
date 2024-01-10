from flask import jsonify,make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt
from ..services import user_service, transaction_service, cart_service, transactionItem_service, product_service
from ..entitys import transaction, transactionItem
from ..models.enumerate import TransactionStatus
from ..schemas import transaction_schema
from API import api

class CompletePurchase(Resource):
    
    @jwt_required()
    def post(self):
        claims = get_jwt()
        user_id = claims['user_id']
        
        user = user_service.list_user_by_id(user_id)
        if user is None:
            return make_response(jsonify("User doesn't exist"), 404)
        
        user_cart = user_service.list_user_by_id(id=user_id).cart
        if not user_cart:
            return make_response(jsonify("The cart is empty."), 404)
        
        total_amount = transaction_service.get_total_amount(user_cart)
        if total_amount == 0 or total_amount is None:
            return make_response(jsonify("User doesn't have items in his cart."), 400)
        
        if user.user_balance < total_amount:
            return make_response(jsonify("Insufficient balance."), 400)
        
        transaction_data = transaction.Transaction(user_id,total_amount,"Purchase")
        user_transaction = transaction_service.make_transaction(transaction_data)
        if user_transaction is not None:
            transaction_service.update_transaction_status_to_completed(user_transaction)
            if user_transaction.status == TransactionStatus.COMPLETED:
                user_service.complete_purchase(user, total_amount)
                items = cart_service.list_cart_by_user(user_id)
                for item in items:
                    product_unit_price = (product_service.list_product_by_id(item.product_id)).unit_price
                    transaction_item = transactionItem.TransactionItem(user_transaction.id,item.product_id, item.quantity, product_unit_price)
                    transactionItem_service.make_transactionItems_history(transaction_item)
                cart_service.clean_user_cart(user)
                ts = transaction_schema.TransactionSchema()
                return make_response(ts.jsonify(user_transaction), 200)
            else:
                transaction_service.delete_transaction(user_transaction)
                return make_response(jsonify("Transaction could not be made"), 500)
        
        transaction_service.update_transaction_status_to_cancelled(user_transaction)
        return make_response(jsonify(message="Transaction failed."), 500)

api.add_resource(CompletePurchase, "/complete-purchase")