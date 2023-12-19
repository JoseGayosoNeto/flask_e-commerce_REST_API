class Product():
    def __init__(self, product_name, description, quantity, unit_price):
        self.__product_name = product_name
        self.__description = description
        self.__quantity = quantity
        self.__unit_price = unit_price

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
    def unit_price(self):
        return self.__unit_price
    
    @unit_price.setter
    def unit_price(self, unit_price):
        self.__unit_price = unit_price