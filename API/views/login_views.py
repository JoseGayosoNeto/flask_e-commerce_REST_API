from API import api, jwt
from ..schemas import login_schema
from flask_restful import Resource
from flask import make_response,jsonify,request
from ..services import user_service
from flask_jwt_extended import create_access_token,create_refresh_token
from datetime import timedelta

class LoginList(Resource):
    
    @jwt.additional_claims_loader
    def add_claims_to_access_token(identity):
        user_token = user_service.list_user_by_id(identity)
        if user_token.is_admin:
            roles = 'admin'
        else:
            roles = 'user'
        
        return {'roles': roles, 'user_id': user_token.id}
    
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            password = request.json['password']
        user_in_db = user_service.list_user_by_email(email)
        
        if user_in_db and user_in_db.verify_password(password):
            access_token = create_access_token(identity=user_in_db.id,expires_delta=timedelta(hours=3))
            refresh_token = create_refresh_token(identity=user_in_db.id)
            return make_response(jsonify({
                'message': 'Login sucessful.',
                'access_token': access_token,
                'refresh_token': refresh_token
            }), 200)
        
        return make_response(jsonify({
            'message': "Login failed due to incorrect email or password"
        }), 401)


api.add_resource(LoginList, '/login')