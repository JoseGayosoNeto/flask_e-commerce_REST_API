from ..models import cart_model
from API import db

def list_cart_by_user(id):
    user_cart = cart_model.Cart.query.filter_by(user_id=id).all()
    return user_cart

def remove_cart_product(product):
    db.session.delete(product)
    db.session.commit()

def insert_new_product_cart(product):
    insert_item_cart = cart_model.Cart(user_id=product.user_id,product_id=product.product_id, quantity=product.quantity)
    db.session.add(insert_item_cart)
    db.session.commit()
    return insert_item_cart

def update_cart_product_quantity(product, quantity):
    product.quantity += quantity
    db.session.commit()
