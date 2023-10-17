from flask_restful import Resource
from API import api,app
from ..schemas import product_schema
from ..entitys import product
from ..services import product_service
from flask import request, make_response, jsonify
import os
class ProductsList(Resource):
    def get(self):
        products = product_service.list_all_products()
        ps = product_schema.ProductSchema(many=True)
        app.logger.info("Listed all products")
        return make_response(ps.jsonify(products), 200)

    def post(self):
        ps = product_schema.ProductSchema()
        validate = ps.validate(request.json) # Performs the validation of data made in schema
        if validate:
            app.logger.info("Validation Error")
            return make_response(jsonify(validate), 400)
        else:
            product_name = request.json['product_name']
            description = request.json['description']
            quantity = request.json['quantity']
            regular_price = request.json['regular_price']

            new_product = product.Product(product_name = product_name,description=description,
                                            quantity=quantity,regular_price=regular_price)
            result = product_service.register_product(new_product)
            aux = ps.jsonify(result)
            app.logger.info(f"Product '{product_name}' registered")
            return make_response(aux, 201)
            

api.add_resource(ProductsList, '/products')