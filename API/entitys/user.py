class User():
    def __init__(self, name, email, password, address, is_admin):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__address = address
        self.__is_admin = is_admin
        self.__user_balance = 0.00
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self, address):
        self.__address = address
    
    @property
    def user_balance(self):
        return self.__user_balance

    @user_balance.setter
    def user_balance(self, user_balance):
        self.__user_balance = user_balance

    @property
    def is_admin(self):
        return self.__is_admin
    
    @is_admin.setter
    def is_admin(self, is_admin):
        self.__is_admin = is_admin



