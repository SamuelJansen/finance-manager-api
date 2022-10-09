from python_framework import Enum, EnumItem


@Enum()
class InvestmentTypeEnumeration:
    LOAN_12R = EnumItem()
    LOAN_10R = EnumItem()
    NONE = EnumItem()


InvestmentType = InvestmentTypeEnumeration()
