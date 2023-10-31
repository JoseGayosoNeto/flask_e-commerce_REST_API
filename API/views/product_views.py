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
            return make_response(aux, 201)
            
class ProductDetails(Resource):
    def get(self, id):
        product = product_service.list_product_by_id(id)
        if product is None:
            return make_response(jsonify("Product doesn't exist."), 404)
        ps = product_schema.ProductSchema()
        return make_response(ps.jsonify(product), 200)

    def put(self, id):
        old_product = product_service.list_product_by_id(id)
        if old_product is None:
            return make_response(jsonify("Product doesn't exist"), 404)
        ps = product_schema.ProductSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            product_name = request.json['product_name']
            description = request.json['description']
            quantity = request.json['quantity']
            regular_price = request.json['regular_price']

            new_product = product.Product(product_name=product_name,description=description,
                                            quantity=quantity,regular_price=regular_price)

            product_service.update_product(old_product, new_product)
            updated_product = product_service.list_product_by_id(id)
            return make_response(ps.jsonify(updated_product), 200)
            

    def delete(self, id):
        product = product_service.list_product_by_id(id)
        if product is None:
            return make_response(jsonify("Product doesn't exist"), 404)
        else:
            product_service.remove_product(product)
            return make_response(jsonify(f"Product '{product.product_name}' sucessfully removed"), 200)



api.add_resource(ProductsList, '/products')
api.add_resource(ProductDetails, '/products/<int:id>')