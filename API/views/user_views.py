from API import api
from ..entitys import user
from ..schemas import user_schema
from ..services import user_service
from flask_restful import Resource
from flask import make_response,jsonify,request

class UserList(Resource):
    # Only for users that have is_admin = True
    def get(self):
        all_users = user_service.list_all_users()
        us = user_schema.UserSchema(many=True)
        return make_response(us.jsonify(all_users), 200)
        
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

    def get(self,id):
        user = user_service.list_user_by_id(id)
        us = user_schema.UserSchema()
        return make_response(us.jsonify(user), 200)
    
    #Admin only
    def delete(self,id):
        user = user_service.list_user_by_id(id)
        if user is None:
            return make_response(jsonify(f"User '{user.name}' doesn't exist "), 404)
        else:
            user_service.delete_user(user)
            return make_response(jsonify(f"User '{user.name}' sucessfully removed"), 200)

class UserDetails_by_email(Resource):
    #Admin only
    def get(self,email):
        user = user_service.list_user_by_email(email)
        us = user_schema.UserSchema()
        return make_response(us.jsonify(user), 200)

api.add_resource(UserList,'/user')
api.add_resource(UserDetails_by_id, '/user/<int:id>')
api.add_resource(UserDetails_by_email, '/user/<string:email>')