class TransactionItem():
    def __init__(self, transaction_id, product_id, quantity, unit_price):
        self.__transaction_id = transaction_id
        self.__product_id = product_id
        self.__quantity = quantity
        self.__unit_price = unit_price
        
    @property
    def transaction_id(self):
        return self.__transaction_id
    
    @transaction_id.setter
    def transaction_id(self,transaction_id):
        self.__transaction_id = transaction_id
    
    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self,product_id):
        self.__product_id = product_id
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    @property
    def unit_price(self):
        return self.__unit_price
    
    @unit_price.setter
    def unit_price(self, unit_price):
        self.__unit_price = unit_price
    
    