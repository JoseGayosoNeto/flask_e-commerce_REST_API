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

