from API import ma
from ..models import cart_model
from marshmallow import fields
from ..services import product_service

class CartSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cart_model.Cart
        load_instance = True
        fields = ('product_id', 'quantity', 'total_value', 'product_name', 'name')

    user_id = fields.Integer(required=False)
    product_id = fields.Integer(required=False)
    quantity = fields.Integer(required=True)
    total_value = fields.Decimal(as_string=True)
    name = fields.Method("get_product_name")
    product_name = fields.String(required=True)
    
    # Return the product_name in the output    
    def get_product_name(self, obj):
        product_name = product_service.list_product_by_id(obj.product_id).product_name
        return product_name