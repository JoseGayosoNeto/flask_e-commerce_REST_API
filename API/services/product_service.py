from ..models import product_model
from API import db

def register_product(product):
    product_bd = product_model.Product(product_name = product.product_name, 
                                        description = product.description, 
                                        quantity = product.quantity, 
                                        regular_price = product.regular_price)
    
    db.session.add(product_bd)
    db.session.commit()
    return product_bd

def list_all_products():
    products = product_model.Product.query.all()
    return products

def list_product_by_id(id):
    product = product_model.Product.query.filter_by(id=id).first()
    return product

def update_product(old_product, new_product):
    old_product.product_name = new_product.product_name
    old_product.description = new_product.description
    old_product.quantity = new_product.quantity
    old_product.regular_price = new_product.regular_price
    db.session.commit()

def remove_product(product):
    db.session.delete(product)
    db.session.commit()
    
def get_product_name_by_id(id):
    return product_model.Product.query.filter_by(id=id).first().product_name