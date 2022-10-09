from python_framework import Mapper, MapperMethod

from model import Executable
from dto import TransactionDto
from helper.static import ExecutorStaticHelper


@Mapper()
class ExecutorMapper:

    @MapperMethod(requestClass=[[TransactionDto.ExecutableTransactionRequestDto]])
    def fromTransactionRequestDtoListToModelList(self, dtoList):
        return [
            self.fromTransactionRequestDtoToModel(model)
            for dto in dtoList
        ]

    @MapperMethod(requestClass=[TransactionDto.ExecutableTransactionRequestDto])
    def fromTransactionRequestDtoToModel(self, dto):
        return Executable.Executable(
            key = ExecutorStaticHelper.buildTransactionKey(dto),
            value = dto
        )
