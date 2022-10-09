from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem

from model import Investment


@Validator()
class InvestmentValidator:

    @ValidatorMethod(requestClass=[Investment.Investment])
    def validateIsFound(self, model):
        if ObjectHelper.isNone(model):
            raise GlobalException(message=f'Investment not found', status=HttpStatus.NOT_FOUND)


    @ValidatorMethod(requestClass=[Investment.Investment])
    def validateIsNotNone(self, model):
        if ObjectHelper.isNone(model):
            raise GlobalException(logMessage=f'Investment cannot be none', status=HttpStatus.INTERNAL_SERVER_ERROR)


    @ValidatorMethod(requestClass=[[Investment.Investment]])
    def validateOnlyOneWasFound(self, modelList):
        if 0 == len(modelList):
            raise GlobalException(message=f'Investment not found', status=HttpStatus.BAD_REQUEST)
        elif 1 < len(modelList):
            raise GlobalException(message=f'Multiple investments were found. Please, refine your query', status=HttpStatus.BAD_REQUEST)
        self.validateIsFound(modelList[0])


    @ValidatorMethod(requestClass=[str])
    def validateDoesNotExistsBYKey(self, key):
        if self.service.investment.existsByKey(key):
            raise GlobalException(message=f'Investment already exists', status=HttpStatus.BAD_REQUEST)
