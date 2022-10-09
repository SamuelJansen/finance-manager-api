from python_framework import Mapper, MapperMethod

from dto import InvestmentDto
from dto import TransactionDto

@Mapper()
class LoanInvestmentMapper:

    @MapperMethod(requestClass=[InvestmentDto.InvestmentResponseDto, [TransactionDto.TransactionResponseDto]], responseClass=[InvestmentDto.LoanInvestmentResponseDto])
    def toResponseDto(self, investmentDto, transactionDtoList, dto):
        dto.transactionList = transactionDtoList
        return dto

    @MapperMethod(requestClass=[[InvestmentDto.InvestmentResponseDto], [TransactionDto.TransactionResponseDto]])
    def toResponseDtoList(self, investmentDtoList, transactionDtoList):
        return [
            self.toResponseDto(
                investmentDto,
                [
                    transactionDto
                    for transactionDto in transactionDtoList
                    if transactionDto.operationKey == investmentDto.key
                ]
            )
            for investmentDto in investmentDtoList
        ]
