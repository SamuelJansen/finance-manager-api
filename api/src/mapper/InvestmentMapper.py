from python_framework import Mapper, MapperMethod, WeekDayConstant, StaticConverter

from model import Investment
from dto import InvestmentDto

@Mapper()
class InvestmentMapper:

    @MapperMethod(requestClass=[[InvestmentDto.InvestmentRequestDto]], responseClass=[[Investment.Investment]])
    def fromRequestDtoListToModelList(self, dtoList, modelList) :
        return modelList

    @MapperMethod(requestClass=[[Investment.Investment]], responseClass=[[InvestmentDto.InvestmentResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[InvestmentDto.InvestmentRequestDto], responseClass=[Investment.Investment])
    def fromRequestDtoToModel(self, dto, model) :
        return model

    @MapperMethod(requestClass=[Investment.Investment], responseClass=[InvestmentDto.InvestmentResponseDto])
    def fromModelToResponseDto(self, model, dto) :
        return dto
