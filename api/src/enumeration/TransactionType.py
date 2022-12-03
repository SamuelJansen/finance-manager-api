from python_framework import Enum, EnumItem


@Enum()
class TransactionTypeEnumeration:
    DEPOSIT = EnumItem()

    INVESTMENT = EnumItem()
    INVESTMENT_RETURN = EnumItem()
    
    PAYMENT = EnumItem()
    WITHDRAW = EnumItem()

    PIX = EnumItem()
    TAD = EnumItem()
    DOC = EnumItem()

    NONE = EnumItem()


TransactionType = TransactionTypeEnumeration()
