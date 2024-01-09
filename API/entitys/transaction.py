from datetime import datetime

class Transaction():
    def __init__(self, user_id, total_amount, transaction_type):
        self.__user_id = user_id
        self.__total_amount = total_amount
        self.__transaction_type = transaction_type
        self.__transaction_date = datetime.now()
        self.__status = "Pending"
        
    @property
    def user_id(self):
        return self.__user_id
    
    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id
    
    @property
    def total_amount(self):
        return self.__total_amount
    
    @total_amount.setter
    def total_amount(self, total_amount):
        self.__total_amount = total_amount
    
    @property
    def transaction_type(self):
        return self.__transaction_type
    
    @transaction_type.setter
    def transaction_type(self, transaction_type):
        self.__transaction_type = transaction_type
        
    @property
    def transaction_date(self):
        return self.__transaction_date
    
    @transaction_date.setter
    def transaction_date(self,transaction_date):
        self.__transaction_date = transaction_date
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status