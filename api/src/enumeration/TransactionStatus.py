from python_framework import Enum, EnumItem


@Enum()
class TransactionStatusEnumeration:
    SCHEADULED = EnumItem()
    PROCESSING = EnumItem()
    PROCESSED = EnumItem()
    REVERTED = EnumItem()
    ERROR = EnumItem()
    NONE = EnumItem()


TransactionStatus = TransactionStatusEnumeration()
