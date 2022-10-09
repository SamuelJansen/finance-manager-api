from python_helper import DateTimeHelper
from python_framework import Mapper, MapperMethod

from enumeration.InvestmentType import InvestmentType
from enumeration.InvestmentStatus import InvestmentStatus
from model import Investment
from dto import InvestmentDto

@Mapper()
class InvestmentMapper:

    @MapperMethod(requestClass=[[InvestmentDto.InvestmentRequestDto]], responseClass=[[Investment.Investment]])
    def fromRequestDtoListToModelList(self, dtoList, modelList):
        return modelList

    @MapperMethod(requestClass=[[Investment.Investment]], responseClass=[[InvestmentDto.InvestmentResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[InvestmentDto.InvestmentRequestDto], responseClass=[Investment.Investment])
    def fromRequestDtoToModel(self, dto, model):
        return model

    @MapperMethod(requestClass=[Investment.Investment], responseClass=[InvestmentDto.InvestmentResponseDto])
    def fromModelToResponseDto(self, model, dto):
        return dto

    @MapperMethod(requestClass=[InvestmentDto.InvestmentResponseDto], responseClass=[InvestmentDto.LoanInvestmentResponseDto])
    def fromResponseDtoToLoanResponseDto(sel, dto, loanDto):
        return loanDto

    @MapperMethod(requestClass=[InvestmentDto.InvestmentRequestDto], responseClass=[Investment.Investment])
    def buildNewModel(self, dto, model):
        model.status = InvestmentStatus.SCHEADULED if model.startAt > DateTimeHelper.now() else InvestmentStatus.PROCESSING
        return model
