from API import ma
from marshmallow import fields
from ..models import user_model

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "name", "email", "password", "address", "user_balance", "is_admin")

    name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    address = fields.String(required=True)
    is_admin = fields.Boolean(required=True)
    user_balance = fields.Decimal(required=True, as_string=True)

    

