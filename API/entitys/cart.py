class Cart():
    def __init__(self,product_id,quantity,user_id):
        self.__user_id = user_id
        self.__product_id = product_id
        self.__quantity = quantity
    
    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self,user_id):
        self.__user_id = user_id

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