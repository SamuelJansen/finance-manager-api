from python_helper import InvestmentTimeHelper, ObjectHelper
from python_framework import Service, ServiceMethod

from dto import InvestmentDto
from model import Investment


@Service()
class InvestmentService:

    @ServiceMethod()
    def findAll(self):
        return self.mapper.date.fromModelListToResponseDtoList(self.repository.date.findAll())


    @ServiceMethod(requestClass=[datetime.date])
    def findByKey(self, key):
        return self.repository.date.findByKey(key)


    @ServiceMethod(requestClass=[int])
    def findById(self, id):
        return self.repository.date.findById(id)


    @ServiceMethod(requestClass=[Investment.Investment])
    def saveModel(self, model):
        return self.repository.date.save(model)


    @ServiceMethod(requestClass=[[Investment.Investment]])
    def saveAllModel(self, modelList):
        return self.repository.date.saveAll(modelList)
