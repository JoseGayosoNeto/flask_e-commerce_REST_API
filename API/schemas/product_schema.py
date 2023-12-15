from API import ma
from ..models import product_model
from marshmallow import fields

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = product_model.Product
        load_instance = True
        fields = ("id", "product_name", "description", "quantity", "unit_price")

    product_name = fields.String(required=True)
    description = fields.String(required=True)
    quantity = fields.Integer(required=True)
    regular_price = fields.Float(required=True)