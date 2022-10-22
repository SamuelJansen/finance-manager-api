from python_helper import DateTimeHelper
from python_framework import Helper, HelperMethod

from constant import MathConstant
from helper.static import MathStaticHelper
from dto import InvestmentDto


class LoanInvestmentHelper:

    @HelperMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto, float, float])
    def getExpectedTotalReturn(self, loanInvestmentDto, historicPercentualReturn, percentualRisk):
        return MathStaticHelper.round(
            loanInvestmentDto.value * (
                (historicPercentualReturn + MathConstant.ONE_HUNDRED_PERCENT) / MathConstant.ONE_HUNDRED_PERCENT
            ) * (
                percentualRisk / MathConstant.ONE_HUNDRED_PERCENT
            )
        )

    @HelperMethod(requestClass=[InvestmentDto.InvestmentResponseDto, int])
    def getExpectedReturnPerTransaction(self, investmentDto, totalReturns):
        return MathStaticHelper.round(investmentDto.expectedReturn / totalReturns)


    @HelperMethod(requestClass=[InvestmentDto.InvestmentResponseDto, float, int, int])
    def getNthInvestmentReturnValue(self, investmentDto, expectedReturnPerTransaction, totalReturns, nthReturn):
        if nthReturn > 1:
            return expectedReturnPerTransaction
        return MathStaticHelper.round(
            investmentDto.expectedReturn - (totalReturns - 1) * expectedReturnPerTransaction
        )


    @HelperMethod(requestClass=[InvestmentDto.InvestmentResponseDto, int])
    def getTransactionAt(self, investmentDto, nthReturn):
        return DateTimeHelper.of(
            date=DateTimeHelper.dateOf(dateTime=DateTimeHelper.plusMonths(investmentDto.startAt, months=nthReturn)),
            time=DateTimeHelper.timeOf(dateTime=investmentDto.startAt)
        )
