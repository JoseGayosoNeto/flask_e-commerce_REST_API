from API import api
from flask_restful import Resource
from flask import make_response,jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import timedelta

class RefreshTokenList(Resource):
    #  Get a new access token with your refresh token without needing to make another 
    #  login request when your token expires
    @jwt_required(refresh=True)
    def post(self):
        user_token = get_jwt_identity()
        access_token = create_access_token(
            identity=user_token,
            expires_delta=timedelta(hours=3)
        )
        refresh_token = create_refresh_token(
            identity=user_token
        )
        
        return make_response(jsonify({
            'new_access_token': access_token,
            'new_refresh_token': refresh_token
        }), 200)
        

api.add_resource(RefreshTokenList, '/token/refresh')