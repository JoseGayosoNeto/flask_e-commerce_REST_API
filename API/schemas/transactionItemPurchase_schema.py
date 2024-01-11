from API import ma
from ..models import transaction_model
from ..services import product_service, transaction_service
from marshmallow import fields

class TransactionItemPurchaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = transaction_model.TransactionItem
        load_instance = True
        fields = ('transaction_id', 'product_name', 'quantity', 'unit_price', 'total_value', 'transaction_type', 'transaction_status')
    
    transaction_id = fields.Integer(required=True)
    product_id = fields.Integer(required=False)
    quantity = fields.Integer(required=True)
    unit_price = fields.Decimal(required=True, as_string=True)
    product_name = fields.Method("get_product_name")
    total_value = fields.Method("get_total_value")
    transaction_type = fields.Method("get_transaction_type")
    transaction_status = fields.Method("get_transaction_status")
    
    def get_product_name(self, obj):
        return (product_service.list_product_by_id(obj.product_id)).product_name
    
    def get_total_value(Self, obj):
        return (obj.quantity * obj.unit_price)
    
    def get_transaction_type(self,obj):
        return (transaction_service.list_transaction_by_transaction_id(obj.transaction_id)).transaction_type.name
    
    def get_transaction_status(self,obj):
        return (transaction_service.list_transaction_by_transaction_id(obj.transaction_id)).status.name