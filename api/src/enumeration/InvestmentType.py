from python_framework import Enum, EnumItem


@Enum()
class InvestmentTypeEnumeration:
    LOAN_12R = EnumItem()
    LOAN_11R = EnumItem()
    LOAN_10R = EnumItem()
    LOAN_09R = EnumItem()
    LOAN_08R = EnumItem()
    LOAN_07R = EnumItem()
    LOAN_06R = EnumItem()
    LOAN_05R = EnumItem()
    LOAN_04R = EnumItem()
    LOAN_03R = EnumItem()
    LOAN_02R = EnumItem()
    LOAN_01R = EnumItem()
    NONE = EnumItem()


InvestmentType = InvestmentTypeEnumeration()
