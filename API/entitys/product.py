class Product():
    def __init__(self, product_name, description, quantity, regular_price):
        self.__product_name = product_name
        self.__description = description
        self.__quantity = quantity
        self.__regular_price = regular_price

    @property
    def product_name(self):
        return self.__product_name
    
    @product_name.setter
    def product_name(self, product_name):
        self.__product_name = product_name
    
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, description):
        self.__description = description
    

    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
    
    @property
    def regular_price(self):
        return self.__regular_price
    
    @regular_price.setter
    def regular_price(self, regular_price):
        self.__regular_price = regular_price