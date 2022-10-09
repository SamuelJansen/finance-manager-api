from python_framework import Mapper, MapperMethod

from model import Balance
from dto import BalanceDto

@Mapper()
class BalanceMapper:

    @MapperMethod(requestClass=[[BalanceDto.BalanceRequestDto]], responseClass=[[Balance.Balance]])
    def fromRequestDtoListToModelList(self, dtoList, modelList):
        return modelList

    @MapperMethod(requestClass=[[Balance.Balance]], responseClass=[[BalanceDto.BalanceResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[BalanceDto.BalanceRequestDto], responseClass=[Balance.Balance])
    def fromRequestDtoToModel(self, dto, model):
        return model

    @MapperMethod(requestClass=[Balance.Balance], responseClass=[BalanceDto.BalanceResponseDto])
    def fromModelToResponseDto(self, model, dto):
        return dto
