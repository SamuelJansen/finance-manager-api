from python_framework import Service, ServiceMethod, EnumItem, StaticConverter

from constant import InvestmentConstant, RiskConstant
from enumeration.InvestmentType import InvestmentType

LOAN_PERCENTUAL_RISK = 80.0

RISK_DICTIONARY = {
    InvestmentType.LOAN_12R: LOAN_PERCENTUAL_RISK,
    InvestmentType.LOAN_10R: LOAN_PERCENTUAL_RISK
}


@Service()
class RiskService:

    @ServiceMethod(requestClass=[EnumItem])
    def getPercentualByIvestmentType(self, investmentType):
        return StaticConverter.getValueOrDefault(
            RISK_DICTIONARY.get(investmentType),
            RiskConstant.DEFAULT_PERCENTUAL_RISK
        )
