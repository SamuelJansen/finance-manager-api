from python_framework import Enum, EnumItem


@Enum()
class InvestmentTypeEnumeration:
    NONE = EnumItem()


InvestmentType = InvestmentTypeEnumeration()
