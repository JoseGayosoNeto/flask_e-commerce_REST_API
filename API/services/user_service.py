from API import db
from ..models import user_model
from decimal import Decimal

def register_new_user(user):
    user_bd = user_model.User(name=user.name,email=user.email,password=user.password,address=user.address,is_admin=user.is_admin, user_balance=user.user_balance)
    user_bd.encrypt_password()
    db.session.add(user_bd)
    db.session.commit()
    return user_bd

def list_all_users():
    return user_model.User.query.all()

def list_user_by_id(id):
    return user_model.User.query.filter_by(id=id).first()

def list_user_by_email(email):
    return user_model.User.query.filter_by(email=email).first()

def delete_user(user):
    db.session.delete(user)
    db.session.commit()

def update_balance(user, value):
    user.user_balance += Decimal(value)
    db.session.commit()