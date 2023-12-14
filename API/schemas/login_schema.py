from API import ma
from marshmallow import fields
from ..models import user_model

class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "name", "email", "password", "address", "user_balance", "is_admin")

    name = fields.String(required=False)
    email = fields.String(required=True)
    password = fields.String(required=True)
    address = fields.String(required=False)
    is_admin = fields.Boolean(required=False)
    user_balance = fields.Decimal(as_string=False)

    

