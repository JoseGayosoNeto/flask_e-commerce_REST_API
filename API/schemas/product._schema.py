from API import ma
from ..models import product_model
from marshmallow import fields

class ProductSchema(ma.SQLAlchemyAutoSchema):
    model = product_model.Product
    load_instance = True
    fields = ("id", "product_name", "description", "image", "quantity", "regular_price")

    product_name = fields.String(required=True)
    description = fields.String(required=True)
    image = fields.String(required=True)
    quantity = fields.Integer(required=True)
    regular_price = fields.Decimal(required=True)