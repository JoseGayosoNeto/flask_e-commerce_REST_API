class Cart():
    def __init__(self,product_id,quantity):
        self.__product_id = product_id
        self.__quantity = quantity
    
    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, product_id):
        self.__product_id = product_id
    
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self,quantity):
        self.__quantity = quantity