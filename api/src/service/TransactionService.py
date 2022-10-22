from python_helper import ObjectHelper
from python_framework import Service, ServiceMethod, Serializer, StaticConverter

from constant import TransactionConstant
from dto import TransactionDto
from model import Transaction

@Service()
class TransactionService:

    @ServiceMethod(requestClass=[TransactionDto.TransactionRequestDto])
    def create(self, dto):
        model = self.mapper.transaction.fromRequestDtoToModel(dto)
        return self.mapper.transaction.fromModelToResponseDto(self.saveModel(model))


    @ServiceMethod(requestClass=[[TransactionDto.TransactionRequestDto]])
    def createAll(self, dtoList):
        modelList = self.mapper.transaction.fromRequestDtoListToModelList(dtoList)
        return self.mapper.transaction.fromModelListToResponseDtoList(self.saveAllModel(modelList))


    @ServiceMethod(requestClass=[TransactionDto.TransactionRequestDto])
    def createScheaduled(self, dto):
        model = self.mapper.transaction.buildNewScheaduledModel(dto)
        return self.mapper.transaction.fromModelToResponseDto(self.saveModel(model))


    @ServiceMethod(requestClass=[[TransactionDto.TransactionRequestDto]])
    def createAllScheaduled(self, dtoList):
        modelList = self.mapper.transaction.buildNewScheaduledModelList(dtoList)
        return self.mapper.transaction.fromModelListToResponseDtoList(self.saveAllModel(modelList))


    @ServiceMethod(requestClass=[TransactionDto.ExecutableTransactionRequestDto])
    def execute(self, dto):
        transactionExecutable = self.service.executor.validateNotInProcessAndAdd(
            self.mapper.executor.fromTransactionRequestDtoToModel(dto)
        )
        model = self.findModelByKey(dto.key)
        self.mapper.transaction.overrideToExecute(model, dto)
        balanceDto = self.service.balance.executeTransactionByKey(model.balanceKey, model.value)
        responseDto = self.mapper.transaction.fromModelToResponseDto(self.saveModel(model))
        self.service.executor.removeIfNeeded(transactionExecutable)
        return responseDto


    @ServiceMethod()
    def findAll(self):
        return self.mapper.transaction.fromModelListToResponseDtoList(self.findAllModel())


    @ServiceMethod(requestClass=[TransactionDto.TransactionQueryDto])
    def findAllByQuery(self, queryDto):
        modelList = self.findAllModelByQuery(queryDto)
        return self.mapper.transaction.fromModelListToResponseDtoList(modelList)


    @ServiceMethod(requestClass=[TransactionDto.TransactionQueryDto])
    def findByQuery(self, queryDto):
        modelList = self.findAllModelByQuery(queryDto)
        self.validator.transaction.validateOnlyOneWasFound(modelList)
        return self.mapper.transaction.fromModelToResponseDto(modelList[0])


    @ServiceMethod(requestClass=[TransactionDto.TransactionQueryDto])
    def findAllModelByQuery(self, queryDto):
        query = Serializer.getObjectAsDictionary(queryDto)
        filteredQuery = {
            k: v
            for k, v in query.items()
            if k not in TransactionConstant.DATE_TIME_QUERY_KEY_LIST
        }
        fromDateTime =  StaticConverter.getValueOrDefault(query.get(TransactionConstant.FROM_DATE_TIME_QUERY_KEY), TransactionConstant.MIN_START_DATE_TIME)
        toDateTime = StaticConverter.getValueOrDefault(query.get(TransactionConstant.TO_DATE_TIME_QUERY_KEY), TransactionConstant.MAX_END_DATE_TIME)
        return self.repository.transaction.findAllByQuery(filteredQuery, fromDateTime, toDateTime)


    @ServiceMethod(requestClass=[[str]])
    def findAllByOperationKeyIn(self, operationKeyList):
        modelList = self.repository.transaction.findAllByOperationKeyIn(operationKeyList)
        return self.mapper.transaction.fromModelListToResponseDtoList(modelList)


    @ServiceMethod(requestClass=[str])
    def findModelByKey(self, key):
        return self.repository.transaction.findByKey(key)


    @ServiceMethod(requestClass=[int])
    def findModelById(self, id):
        return self.repository.transaction.findById(id)


    @ServiceMethod()
    def findAllModel(self):
        return self.repository.transaction.findAll()


    @ServiceMethod(requestClass=[Transaction.Transaction])
    def saveModel(self, model):
        return self.repository.transaction.save(model)


    @ServiceMethod(requestClass=[[Transaction.Transaction]])
    def saveAllModel(self, modelList):
        return self.repository.transaction.saveAll(modelList)
