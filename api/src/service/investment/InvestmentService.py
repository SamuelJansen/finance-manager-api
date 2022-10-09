from python_helper import DateTimeHelper
from python_framework import Service, ServiceMethod, EnumItem

from enumeration.InvestmentType import InvestmentType
from dto import InvestmentDto, TransactionDto
from model import Investment


@Service()
class InvestmentService:

    @ServiceMethod(requestClass=[InvestmentDto.InvestmentRequestDto])
    def create(self, dto):
        self.validator.investment.validateDoesNotExistsBYKey(dto.key)
        model = self.saveModel(self.mapper.investment.buildNewModel(dto))
        return self.mapper.investment.fromModelToResponseDto(model)


    @ServiceMethod()
    def findAll(self):
        return self.mapper.investment.fromModelListToResponseDtoList(self.findAllModel())


    @ServiceMethod(requestClass=[[EnumItem]])
    def findAllByTypeIn(self, typeList):
        modelList = self.repository.investment.findAllByTypeIn(typeList)
        return self.mapper.investment.fromModelListToResponseDtoList(modelList)


    @ServiceMethod(requestClass=[str, [EnumItem]])
    def findAllByKeyAndTypeIn(self, key, typeList):
        modelList = self.repository.investment.findAllByKeyAndTypeIn(key, typeList)
        self.validator.investment.validateOnlyOneWasFound(modelList)
        return self.mapper.investment.fromModelToResponseDto(modelList[0])


    @ServiceMethod(requestClass=[[str], [EnumItem]])
    def findAllByKeyInAndTypeIn(self, keyList, typeList):
        modelList = self.repository.investment.findAllByKeyInAndTypeIn(keyList, typeList)
        return self.mapper.investment.fromModelListToResponseDtoList(modelList)


    @ServiceMethod(requestClass=[str])
    def findModelByKey(self, key):
        return self.repository.investment.findByKey(key)


    @ServiceMethod(requestClass=[int])
    def findModelById(self, id):
        return self.repository.investment.findById(id)


    @ServiceMethod()
    def findAllModel(self):
        return self.repository.investment.findAll()


    @ServiceMethod(requestClass=[str])
    def existsByKey(self, key):
        return self.repository.investment.existsByKey(key)


    @ServiceMethod(requestClass=[Investment.Investment])
    def saveModel(self, model):
        return self.repository.investment.save(model)


    @ServiceMethod(requestClass=[[Investment.Investment]])
    def saveAllModel(self, modelList):
        return self.repository.investment.saveAll(modelList)
