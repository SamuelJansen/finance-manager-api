from python_helper import DateTimeHelper
from python_framework import Mapper, MapperMethod, StaticConverter

from enumeration.TransactionType import TransactionType
from enumeration.TransactionStatus import TransactionStatus
from model import Transaction
from dto import TransactionDto

@Mapper()
class TransactionMapper:

    @MapperMethod(requestClass=[[TransactionDto.TransactionRequestDto]], responseClass=[[Transaction.Transaction]])
    def fromRequestDtoListToModelList(self, dtoList, modelList):
        return modelList

    @MapperMethod(requestClass=[[Transaction.Transaction]], responseClass=[[TransactionDto.TransactionResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[TransactionDto.TransactionRequestDto], responseClass=[Transaction.Transaction])
    def fromRequestDtoToModel(self, dto, model):
        return model

    @MapperMethod(requestClass=[Transaction.Transaction], responseClass=[TransactionDto.TransactionResponseDto])
    def fromModelToResponseDto(self, model, dto):
        return dto

    @MapperMethod(requestClass=[TransactionDto.TransactionRequestDto], responseClass=[Transaction.Transaction])
    def buildNewScheaduledModel(self, dto, model):
        model.status = TransactionStatus.SCHEADULED if model.transactionAt > DateTimeHelper.now() else TransactionStatus.PROCESSING
        return model

    @MapperMethod(requestClass=[[TransactionDto.TransactionRequestDto]])
    def buildNewScheaduledModelList(self, dtoList):
        return [
            self.buildNewScheaduledModel(dto)
            for dto in dtoList
        ]

    @MapperMethod(requestClass=[Transaction.Transaction, TransactionDto.ExecutableTransactionRequestDto])
    def overrideToExecute(self, model, dto):
        model.value = StaticConverter.getValueOrDefault(dto.value, model.value)
        model.transactionAt = StaticConverter.getValueOrDefault(dto.transactionAt, model.transactionAt)
        model.status = TransactionStatus.PROCESSED
        return model
