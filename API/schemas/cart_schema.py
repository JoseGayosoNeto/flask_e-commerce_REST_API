from API import ma
from ..models import cart_model
from marshmallow import fields
from ..services import product_service

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cart_model.Cart
        load_instance = True
        fields = ('product_id', 'quantity', 'total_value', 'product_name')

    user_id = fields.Integer(required=False)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_value = fields.Decimal(as_string=True)
    product_name = fields.Method("get_product_name")
    
    def get_product_name(self, obj):
        product_name = product_service.get_product_name_by_id(obj.product_id)
        return product_name