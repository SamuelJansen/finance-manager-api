from python_framework import Service, ServiceMethod, EnumItem, StaticConverter

from constant import HistoryConstant
from enumeration.InvestmentType import InvestmentType


LOAN_PERCENTUAL_RETURN = 30.0

RISK_DICTIONARY = {
    InvestmentType.LOAN_12R: LOAN_PERCENTUAL_RETURN,
    InvestmentType.LOAN_10R: LOAN_PERCENTUAL_RETURN
}


@Service()
class HistoryService:

    @ServiceMethod(requestClass=[EnumItem])
    def getPercentualByIvestmentType(self, investmentType):
        return StaticConverter.getValueOrDefault(
            RISK_DICTIONARY.get(investmentType),
            HistoryConstant.DEFAULT_PERCENTUAL_RETURN
        )
