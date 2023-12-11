from API import ma
from ..models import cart_model
from ..schemas import product_schema
from marshmallow import fields

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cart_model.Cart
        load_instance = True
        fields = ('product_id', 'quantity', 'total_value', 'user_id')


    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_value = fields.Decimal(as_string=True)