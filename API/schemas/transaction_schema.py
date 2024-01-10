from API import ma
from ..models import transaction_model
from marshmallow import fields, validate
from ..services import user_service

class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = transaction_model.Transaction
        load_instance = True
        fields = ('id', 'transaction_user', 'total_amount', 'transaction_date', 'transaction_type', 'status')
    
    id = fields.Integer(required=False)
    user_id = fields.Integer(required=False)
    total_amount = fields.Decimal(required=False, as_string=True)
    transaction_date = fields.DateTime(required=False, format= "%d/%m/%Y, %H:%M:%S")
    transaction_type = fields.Method("get_transaction_type")
    status = fields.Method("get_status")
    transaction_user = fields.Method("get_user_name")
    
    def get_transaction_type(self,obj):
        return obj.transaction_type.name
    
    def get_status(self, obj):
        return obj.status.name
    def get_user_name(self,obj):
        return user_service.list_user_by_id(obj.user_id).name