from enum import Enum

class TransactionType(Enum):
    BALANCE = "Balance"
    PURCHASE = "Purchase"

class TransactionStatus(Enum):
    COMPLETED = "Completed"
    PENDING = "Pending"
    CANCELLED = "Cancelled"