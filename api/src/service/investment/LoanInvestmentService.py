from python_helper import DateTimeHelper
from python_framework import Service, ServiceMethod

from constant import InvestmentConstant, MathConstant
from enumeration.InvestmentType import InvestmentType
from enumeration.TransactionType import TransactionType
from helper.static import MathStaticHelper
from dto import InvestmentDto, TransactionDto
from model import Investment


@Service()
class LoanInvestmentService:

    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto])
    def create(self, dto):
        investmentDto = self.createInvestment(dto)
        transactionDtoList = []
        if InvestmentType.LOAN_12R == investmentDto.type:
            transactionDtoList = self.scheaduleTransactions(investmentDto, 12)
        if InvestmentType.LOAN_10R == investmentDto.type:
            transactionDtoList = self.scheaduleTransactions(investmentDto, 10)
        return self.mapper.loanInvestment.toResponseDto(investmentDto, transactionDtoList)


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentQueryRequestDto])
    def findByQuery(self, paramDto):
        investmentDto = self.service.investment.findAllByKeyAndTypeIn(paramDto.key, InvestmentConstant.LOAN_INVESTMENT_LIST)
        transactionDtoList = self.getInvestmentTransactionDtoList([investmentDto])
        return self.mapper.loanInvestment.toResponseDto(investmentDto, transactionDtoList)


    @ServiceMethod()
    def findAll(self):
        investmentDtoList = self.service.investment.findAllByTypeIn(InvestmentConstant.LOAN_INVESTMENT_LIST)
        transactionDtoList = self.getInvestmentTransactionDtoList(investmentDtoList)
        return self.mapper.loanInvestment.toResponseDtoList(investmentDtoList, transactionDtoList)


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentQueryAllRequestDto])
    def findAllByQuery(self, paramDto):
        investmentDtoList = self.service.investment.findAllByKeyInAndTypeIn(paramDto.keyList, InvestmentConstant.LOAN_INVESTMENT_LIST)
        transactionDtoList = self.getInvestmentTransactionDtoList(investmentDtoList)
        return self.mapper.loanInvestment.toResponseDtoList(investmentDtoList, transactionDtoList)


    @ServiceMethod(requestClass=[[InvestmentDto.InvestmentResponseDto]])
    def getInvestmentTransactionDtoList(self, investmentDtoList):
        operationKeyList = list(set([
            investmentDto.key
            for investmentDto in investmentDtoList
        ]))
        return self.service.transaction.findAllByOperationKeyIn(operationKeyList)


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto])
    def createInvestment(self, dto):
        print(self.getExpectedTotalReturn(dto))
        return self.service.investment.create(
            InvestmentDto.InvestmentRequestDto(
                key = dto.key,
                balanceKey = dto.balanceKey,
                startAt = dto.startAt,
                type = dto.type,
                value = dto.value,
                expectedReturn = self.getExpectedTotalReturn(dto),
                risk = self.service.risk.getPercentualByIvestmentType(dto.type),
            )
        )


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentRequestDto, int])
    def scheaduleTransactions(self, investmentDto, totalReturns):
        expectedReturnPerTransaction = MathStaticHelper.round(investmentDto.expectedReturn / totalReturns)
        print(f'{investmentDto.expectedReturn=}')
        print(f'{totalReturns=}')
        print(f'{expectedReturnPerTransaction=}')
        return [
            self.service.transaction.create(
                self.mapper.transaction.buildNewScheaduledTransaction(
                    TransactionDto.TransactionRequestDto(
                        operationKey = investmentDto.key,
                        balanceKey = investmentDto.balanceKey,
                        value = -1 * investmentDto.value,
                        transactionAt = DateTimeHelper.now()
                    ),
                    TransactionType.INVESTMENT
                )
            ),
            *self.service.transaction.createAll([
                self.mapper.transaction.buildNewScheaduledTransaction(
                    TransactionDto.TransactionRequestDto(
                        operationKey = investmentDto.key,
                        balanceKey = investmentDto.balanceKey,
                        value = self.getNthInvestmentReturnValue(investmentDto, expectedReturnPerTransaction, totalReturns, nthReturn),
                        transactionAt = DateTimeHelper.of(
                            date=DateTimeHelper.dateOf(dateTime=self.getReturnDate(investmentDto, nthReturn)),
                            time=DateTimeHelper.timeOf(dateTime=investmentDto.startAt)
                        )
                    ),
                    TransactionType.INVESTMENT_RETURN
                )
                for nthReturn in range(1, totalReturns + 1)
            ])
        ]


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto])
    def getExpectedTotalReturn(self, dto):
        print('    ', dto.value)
        print('    ', self.service.history.getPercentualByIvestmentType(dto.type))
        print('    ', (self.service.history.getPercentualByIvestmentType(dto.type) + MathConstant.ONE_HUNDRED_PERCENT) / MathConstant.ONE_HUNDRED_PERCENT)
        print('    ', self.service.risk.getPercentualByIvestmentType(dto.type))
        print('    ', self.service.risk.getPercentualByIvestmentType(dto.type) / MathConstant.ONE_HUNDRED_PERCENT)
        return MathStaticHelper.round(
            dto.value * (
                (self.service.history.getPercentualByIvestmentType(dto.type) + MathConstant.ONE_HUNDRED_PERCENT) / MathConstant.ONE_HUNDRED_PERCENT)
            ) * (
                self.service.risk.getPercentualByIvestmentType(dto.type) / MathConstant.ONE_HUNDRED_PERCENT
            )


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentRequestDto, float, int, int])
    def getNthInvestmentReturnValue(self, investmentDto, expectedReturnPerTransaction, totalReturns, nthReturn):
        print(f'        {expectedReturnPerTransaction=}')
        print(f'        {nthReturn=}')
        print(f'        {totalReturns=}')
        print(f'        {investmentDto.expectedReturn}')
        return expectedReturnPerTransaction if nthReturn > 1 else investmentDto.expectedReturn - (totalReturns - 1) * expectedReturnPerTransaction


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentResponseDto, int])
    def getReturnDate(self, investmentDto, nthReturn):
        date = DateTimeHelper.dateOf(dateTime=DateTimeHelper.plusMonths(investmentDto.startAt, months=nthReturn))
        return DateTimeHelper.of(date=date, time=DateTimeHelper.DEFAULT_TIME_END)
