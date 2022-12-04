from python_helper import DateTimeHelper, ObjectHelper
from python_framework import Service, ServiceMethod, StaticConverter

from constant import InvestmentConstant
from enumeration.InvestmentType import InvestmentType
from enumeration.TransactionType import TransactionType
from helper.static import LoanInvestmentStaticHelper
from dto import InvestmentDto, TransactionDto
from model import Investment


@Service()
class LoanInvestmentService:

    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto])
    def create(self, dto):
        investmentDto = self.createInvestment(dto)
        transactionDtoList = self.createTransactionList(investmentDto)
        return self.mapper.loanInvestment.toResponseDto(investmentDto, transactionDtoList)

    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentQueryDto])
    def findByQuery(self, queryDto):
        userData = self.service.security.getUserData()
        investmentDtoList = self.service.investment.findAllByQuery(
            InvestmentDto.InvestmentQueryAllDto(
                userKey = userData.key,
                keyList = [queryDto.key] if ObjectHelper.isNotNone(queryDto.key) else [],
                labelList = [queryDto.label] if ObjectHelper.isNotNone(queryDto.label) else [],
                typeList = InvestmentConstant.LOAN_INVESTMENT_LIST
            )
        )
        self.validator.investment.validateOnlyOneWasFound(investmentDto)
        investmentDto = investmentDtoList[0]
        transactionDtoList = self.getInvestmentTransactionDtoList([investmentDto])
        return self.mapper.loanInvestment.toResponseDto(investmentDto, transactionDtoList)


    @ServiceMethod()
    def findAll(self):
        investmentDtoList = self.service.investment.findAllByTypeIn(InvestmentConstant.LOAN_INVESTMENT_LIST)
        transactionDtoList = self.getInvestmentTransactionDtoList(investmentDtoList)
        return self.mapper.loanInvestment.toResponseDtoList(investmentDtoList, transactionDtoList)


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentQueryAllDto])
    def findAllByQuery(self, queryDto):
        investmentDtoList = self.service.investment.findAllByKeyInAndTypeIn(queryDto.keyList, InvestmentConstant.LOAN_INVESTMENT_LIST)
        transactionDtoList = self.getInvestmentTransactionDtoList(investmentDtoList)
        return self.mapper.loanInvestment.toResponseDtoList(investmentDtoList, transactionDtoList)


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto])
    def createInvestment(self, dto):
        return self.service.investment.create(
            InvestmentDto.InvestmentRequestDto(
                key = dto.key,
                userKey = dto.userKey,
                balanceKey = dto.balanceKey,
                label = dto.label,
                value = dto.value,
                startAt = dto.startAt,
                type = dto.type,
                expectedReturn = self.getExpectedTotalReturn(dto),
                risk = self.service.risk.getPercentualByIvestmentType(dto.type),
            )
        )


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentResponseDto])
    def createTransactionList(self, investmentDto):
        if investmentDto.type in InvestmentConstant.LOAN_INVESTMENT_LIST:
            totalReturns = LoanInvestmentStaticHelper.parseTotalReturns(investmentDto.type.enumName)
            return self.scheaduleTransactions(investmentDto, totalReturns)


    @ServiceMethod(requestClass=[[InvestmentDto.InvestmentResponseDto]])
    def getInvestmentTransactionDtoList(self, investmentDtoList):
        operationKeyList = LoanInvestmentStaticHelper.getUniqueOperationKeyList(investmentDtoList)
        return self.service.transaction.findAllByOperationKeyIn(operationKeyList)


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentResponseDto, int])
    def scheaduleTransactions(self, investmentDto, totalReturns):
        expectedReturnPerTransaction = self.helper.loanInvestment.getExpectedReturnPerTransaction(investmentDto, totalReturns)
        return [
            self.service.transaction.createScheaduled(
                TransactionDto.TransactionRequestDto(
                    userKey = investmentDto.userKey,
                    operationKey = investmentDto.key,
                    balanceKey = investmentDto.balanceKey,
                    value = -1 * investmentDto.value,
                    transactionAt = self.helper.loanInvestment.getTransactionAt(investmentDto, InvestmentConstant.LOAN_APPORT_TRANSACTION),
                    type = TransactionType.INVESTMENT
                )
            ),
            *self.service.transaction.createAllScheaduled([
                TransactionDto.TransactionRequestDto(
                    userKey = investmentDto.userKey,
                    operationKey = investmentDto.key,
                    balanceKey = investmentDto.balanceKey,
                    value = self.helper.loanInvestment.getNthInvestmentReturnValue(investmentDto, expectedReturnPerTransaction, totalReturns, nthReturn),
                    transactionAt = self.helper.loanInvestment.getTransactionAt(investmentDto, nthReturn),
                    type = TransactionType.INVESTMENT_RETURN
                )
                for nthReturn in LoanInvestmentStaticHelper.getTotalReturnsRange(totalReturns)
            ])
        ]


    @ServiceMethod(requestClass=[InvestmentDto.LoanInvestmentRequestDto])
    def getExpectedTotalReturn(self, dto):
        historicPercentualReturn = self.service.history.getPercentualByIvestmentType(dto.type)
        percentualRisk = self.service.risk.getPercentualByIvestmentType(dto.type)
        return self.helper.loanInvestment.getExpectedTotalReturn(dto, historicPercentualReturn, percentualRisk)
