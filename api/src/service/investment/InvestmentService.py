from python_helper import DateTimeHelper
from python_framework import Service, ServiceMethod, EnumItem, Serializer

from enumeration.InvestmentType import InvestmentType
from dto import InvestmentDto, TransactionDto
from model import Investment


@Service()
class InvestmentService:

    @ServiceMethod(requestClass=[InvestmentDto.InvestmentRequestDto])
    def create(self, dto):
        self.validator.investment.validateCreate(dto)
        model = self.saveModel(self.mapper.investment.buildNewModel(dto))
        return self.mapper.investment.fromModelToResponseDto(model)


    @ServiceMethod()
    def findAll(self):
        return self.mapper.investment.fromModelListToResponseDtoList(self.findAllModel())


    @ServiceMethod(requestClass=[[EnumItem]])
    def findAllByTypeIn(self, typeList):
        userData = self.service.security.getUserData()
        modelList = self.mapper.investment.fromModelListToResponseDtoList(
            self.findAllModelByQuery(
                InvestmentDto.InvestmentQueryAllDto(
                    userKey = userData.key,
                    typeList = typeList
                )
            )
        )
        return self.mapper.investment.fromModelListToResponseDtoList(modelList)


    @ServiceMethod(requestClass=[str, [EnumItem]])
    def findAllByKeyAndTypeIn(self, key, typeList):
        userData = self.service.security.getUserData()
        modelList = self.mapper.investment.fromModelListToResponseDtoList(
            self.findAllModelByQuery(
                InvestmentDto.InvestmentQueryAllDto(
                    userKey = userData.key,
                    keyList = [key],
                    typeList = typeList
                )
            )
        )
        self.validator.investment.validateOnlyOneWasFound(modelList)
        return self.mapper.investment.fromModelToResponseDto(modelList[0])


    @ServiceMethod(requestClass=[[str], [EnumItem]])
    def findAllByKeyInAndTypeIn(self, keyList, typeList):
        userData = self.service.security.getUserData()
        return self.mapper.investment.fromModelListToResponseDtoList(
            self.findAllModelByQuery(
                InvestmentDto.InvestmentQueryAllDto(
                    userKey = userData.key,
                    keyList = keyList,
                    typeList = typeList
                )
            )
        )


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentQueryAllDto])
    def findAllByQuery(self, queryAllDto):
        return self.mapper.investment.fromModelListToResponseDtoList(
            self.findAllModelByQuery(queryAllDto)
        )


    @ServiceMethod(requestClass=[InvestmentDto.InvestmentQueryAllDto])
    def findAllModelByQuery(self, queryAllDto):
        userData = self.validator.investment.validateFindAllByQuery(queryAllDto)
        query = Serializer.getObjectAsDictionary(queryAllDto)
        return self.repository.investment.findAllByQuery(query)


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


    @ServiceMethod(requestClass=[[str], str])
    def existsByLabelInAndUserKey(self, labelList, userKey):
        query = Serializer.getObjectAsDictionary(
            InvestmentDto.InvestmentQueryAllDto(
                userKey = userKey,
                labelList = labelList
            )
        )
        return self.repository.investment.existsByQuery(query)


    @ServiceMethod(requestClass=[Investment.Investment])
    def saveModel(self, model):
        return self.repository.investment.save(model)


    @ServiceMethod(requestClass=[[Investment.Investment]])
    def saveAllModel(self, modelList):
        return self.repository.investment.saveAll(modelList)
