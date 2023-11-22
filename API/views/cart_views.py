from flask_restful import Resource
from ..entitys import cart
from ..entitys.product import Product
from ..schemas import cart_schema
from ..services import cart_service, product_service
from ..models import product_model, cart_model
from API import api,app
from flask import make_response, jsonify, request

class ManageDetails(Resource):

    def get(self,id): # Get user cart by id
        user_cart = cart_service.list_cart_by_user(id)
        cs = cart_schema.CartSchema(many=True)
        return make_response(cs.jsonify(user_cart), 200)

class ManageCart(Resource):
    def post(self):
        cs = cart_schema.CartSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            user_id = request.json['user_id']
            product_id = request.json['product_id']
            quantity = request.json['quantity']

            #product = product_model.Product.query.filter_by(id=product_id).first()
            product = product_service.list_product_by_id(product_id)
            if product is None:
                return make_response(jsonify("Product doesn't exist"), 404)
            else:
                storage = int(product.quantity)
                if not storage:
                    return make_response(jsonify("Out of storage"), 400)
                item = cart_service.search_product_in_cart(user_id=user_id,product_id=product_id)
                # Item already exists in cart
                if item: 
                    # Item with quantity = 0 in cart -> Remove item from cart
                    if not quantity:
                        cart_service.remove_cart_product(item)
                        # Returning product quantity to storage
                        storage_product = product_service.list_product_by_id(product_id)
                        new_storage_product = Product(product_name=storage_product.product_name,
                                                    description=storage_product.description,
                                                    quantity=storage_product.quantity+item.quantity,
                                                    regular_price=storage_product.regular_price)
                                                    
                        product_service.update_product(storage_product,new_storage_product)

                        return make_response(jsonify(f"Item '{storage_product.product_name}' has been removed from cart"), 200)

                    # If item already exists in cart, just update his values on the db
                    # Adds more quantity of a item in cart and reduce it in storage 
                    # If quantity added was < 0, then remove the quantity for the actual quantity on storage
                    cart_service.update_cart_product_quantity(item,quantity)
                    # Removing product quantity in store
                    old_product = product_service.list_product_by_id(product_id)
                    new_product = Product(product_name=old_product.product_name,
                                        description=old_product.description,
                                        quantity=old_product.quantity-quantity,
                                        regular_price=old_product.regular_price)

                    if new_product.quantity < 0:
                        return make_response(jsonify(f"Quantity of the product '{new_product.product_name}' in the cart exceeded the quantity in stock"), 400)

                    product_service.update_product(old_product,new_product)

                    cs = cart_schema.CartSchema(many=True)
                    result = cart_service.list_cart_by_user(user_id)
                    aux = cs.jsonify(result)

                    return make_response(aux,201)
                
                else: # Item doesn't exist in cart
                    # Your quantity is invalid
                    if not quantity:
                        return make_response(jsonify('Quantity invalid'), 400)
                    
                    # Product quantity in cart < 0
                    if quantity < 0:
                        return make_response(jsonify("There is no quantity of this product in the cart"), 400)
                    # Adding a new product to the user cart
                    item = cart.Cart(user_id=user_id,product_id=product_id,quantity=quantity)

                    if quantity > storage:
                        return make_response(jsonify("This quantity is not in store"), 400)
                    
                    # Add new product and his quantity to the cart
                    result = cart_service.insert_new_product_cart(item)
                    # Removing product quantity in store
                    old_product = product_service.list_product_by_id(product_id)
                    new_product = Product(product_name=old_product.product_name,description=old_product.description,
                                        quantity=old_product.quantity-item.quantity,regular_price=old_product.regular_price)
                    product_service.update_product(old_product,new_product)

                    cs = cart_schema.CartSchema(many=True)
                    user_cart = cart_service.list_cart_by_user(id=user_id)
                    aux = cs.jsonify(user_cart)
                    return make_response(aux, 201)


api.add_resource(ManageDetails, '/cart_details/user/<int:id>')
api.add_resource(ManageCart, '/manage_cart')


