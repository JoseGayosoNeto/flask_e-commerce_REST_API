from flask_restful import Resource
from API import api,app

class ProductsList(Resource):
    def get(self):
        app.logger.info("Mensagem teste")
        return 'hello world!'


api.add_resource(ProductsList, '/products')