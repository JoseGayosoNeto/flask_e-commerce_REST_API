from API import api
from ..entitys import user, transaction
from ..schemas import user_schema, transaction_schema
from ..services import user_service, transaction_service
from ..models.user_model import User
from flask_restful import Resource
from flask import make_response,jsonify,request
from ..paginate import paginate
from flask_jwt_extended import jwt_required, get_jwt
from ..decorator import admin_required
from ..models.enumerate import TransactionStatus

class UserList(Resource):
    @admin_required
    def get(self):
        us = user_schema.UserSchema(many=True)
        return paginate(User, us)
        
    def post(self):
        us = user_schema.UserSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json['name']
            email = request.json['email']
            password = request.json['password']
            address = request.json['address']
            is_admin = request.json['is_admin']

            new_user = user.User(name=name,email=email,password=password,address=address,is_admin=is_admin)
            result = user_service.register_new_user(new_user)
            aux = us.jsonify(result)
            return make_response(aux, 201)

class UserDetails_by_id(Resource):
    @admin_required
    def get(self,id):
        user = user_service.list_user_by_id(id)
        us = user_schema.UserSchema()
        return make_response(us.jsonify(user), 200)
    
    @admin_required
    def delete(self,id):
        user = user_service.list_user_by_id(id)
        if user is None:
            return make_response(jsonify(f"User doesn't exist "), 404)
        else:
            user_service.delete_user(user)
            return make_response(jsonify(f"User '{user.name}' sucessfully removed"), 200)

class UserDetails_by_email(Resource):
    @admin_required
    def get(self,email):
        user = user_service.list_user_by_email(email)
        us = user_schema.UserSchema()
        return make_response(us.jsonify(user), 200)
    
    @admin_required
    def delete(sef,email):
        user = user_service.list_user_by_email(email)
        if user is None:
            return make_response(jsonify(f"User doesn't exist."), 404)
        else:
            user_service.delete_user(user)
            return make_response(jsonify(f"User {user.name} sucessfully removed"), 200)

class Update_User_Balance(Resource):
    @jwt_required()
    def patch(self):
        claims = get_jwt()
        user_id = claims['user_id']
        user = user_service.list_user_by_id(user_id)
        if user is None:
            return make_response(jsonify(f"User doesn't exist"), 404)
        else:
            us = user_schema.UserSchema(only=["amount_to_add"])
            validate = us.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 400)
            
            amount_to_add = request.json['amount_to_add']
            if amount_to_add <= 0:
                return make_response(jsonify(message="The amount entered cannot be negative or zero. Please enter a valid amount to add to your account."), 400)
            
            transaction_data = transaction.Transaction(user_id,amount_to_add, "Balance")
            user_transaction = transaction_service.make_transaction(transaction_data)
            if user_transaction is not None:
                transaction_service.update_transaction_status_to_completed(user_transaction)
                if user_transaction.status == TransactionStatus.COMPLETED:
                    user_service.update_balance(user, amount_to_add)
                    return make_response(jsonify({"message": "User balance update sucessful.",
                                    "new_user_balance": user.user_balance
                                    }), 200)
                else:
                    transaction_service.delete_transaction(user_transaction)
                    return make_response(jsonify("Transaction could not be made."), 400)
            transaction_service.update_transaction_status_to_cancelled(user_transaction)
            return make_response(jsonify(message="Transaction failed."), 500)
            
class YourUserDetails(Resource):

    @jwt_required()
    def get(self):
        claims = get_jwt()
        user_id = claims['user_id']
        user = user_service.list_user_by_id(user_id)
        us = user_schema.UserSchema()
        return make_response(us.jsonify(user), 200)

class UserTransactionDetails(Resource):
    
    @jwt_required()
    def get(self):
        claims = get_jwt()
        user_id = claims['user_id']
        user_transactions = transaction_service.list_transactions_by_user_id(user_id)
        ts = transaction_schema.TransactionSchema(many=True)
        return make_response(ts.jsonify(user_transactions), 200)

api.add_resource(UserList,'/user')
api.add_resource(UserDetails_by_id, '/user/<int:id>')
api.add_resource(UserDetails_by_email, '/user/<string:email>')
api.add_resource(Update_User_Balance, '/user/update_balance')
api.add_resource(YourUserDetails, '/user/details')
api.add_resource(UserTransactionDetails, '/user/transactions')