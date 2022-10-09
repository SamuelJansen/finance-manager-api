from constant import RiskConstant
from enumeration.InvestmentType import InvestmentType
from enumeration.InvestmentStatus import InvestmentStatus

DEFAULT_VALUE = 0.0
DEFAULT_EXPECTED_RETURN = 0.0
DEFAULT_PERCENTUAL_RISK = RiskConstant.DEFAULT_PERCENTUAL_RISK
DEFAULT_TYPE = InvestmentType.NONE
DEFAULT_STATUS = InvestmentStatus.NONE

LOAN_INVESTMENT_LIST = [
    InvestmentType.LOAN_12R,
    InvestmentType.LOAN_10R
]
