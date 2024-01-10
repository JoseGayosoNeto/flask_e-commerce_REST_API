from API import ma
from marshmallow import fields
from ..models import user_model

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "name", "email", "password", "address", "amount_to_add", "is_admin", "user_balance")

    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    address = fields.String(required=True)
    is_admin = fields.Boolean(required=True)
    amount_to_add = fields.Decimal(as_string=True)
    user_balance = fields.Decimal(as_string=True)

    

