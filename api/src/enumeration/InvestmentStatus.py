from python_framework import Enum, EnumItem


@Enum()
class InvestmentStatusEnumeration:
    SCHEADULED = EnumItem()
    PROCESSING = EnumItem()
    PROCESSED = EnumItem()
    REVERTED = EnumItem()
    ERROR = EnumItem()
    NONE = EnumItem()


InvestmentStatus = InvestmentStatusEnumeration()
