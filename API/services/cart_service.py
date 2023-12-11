from ..models import cart_model
from ..services import product_service
from API import db

def list_cart_by_user(id):
    user_cart = cart_model.Cart.query.filter_by(user_id=id).all()
    return user_cart

def remove_cart_product(item):
    db.session.delete(item)
    db.session.commit()

def insert_new_product_cart(item):
    item_data = product_service.list_product_by_id(item.product_id)
    insert_item_cart = cart_model.Cart(user_id=item.user_id,product_id=item.product_id, quantity=item.quantity, total_value=(item.quantity*item_data.regular_price))
    db.session.add(insert_item_cart)
    db.session.commit()
    return insert_item_cart

def update_cart_product_quantity(item, quantity):
    item.quantity += quantity
    db.session.commit()

def search_product_in_cart(user_id,product_id):
    cart = cart_model.Cart.query.filter_by(product_id=product_id,user_id=user_id).first()
    return cart

def update_item_value(item):
    product = product_service.list_product_by_id(item.product_id)
    item.total_value = item.quantity * product.regular_price
    db.session.commit()
    