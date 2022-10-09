from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem

from model import Transaction


@Validator()
class TransactionValidator:

    @ValidatorMethod(requestClass=[Transaction.Transaction])
    def validateIsFound(self, model):
        if ObjectHelper.isNone(model):
            raise GlobalException(message=f'Transaction not found', status=HttpStatus.NOT_FOUND)


    @ValidatorMethod(requestClass=[Transaction.Transaction])
    def validateIsNotNone(self, model):
        if ObjectHelper.isNone(model):
            raise GlobalException(logMessage=f'Transaction cannot be none', status=HttpStatus.INTERNAL_SERVER_ERROR)


    @ValidatorMethod(requestClass=[[Transaction.Transaction]])
    def validateOnlyOneWasFound(self, modelList):
        if 0 == len(modelList):
            raise GlobalException(message=f'Transaction not found', status=HttpStatus.BAD_REQUEST)
        elif 1 < len(modelList):
            raise GlobalException(message=f'Multiple transactions were found. Please, refine your query', status=HttpStatus.BAD_REQUEST)
        self.validateIsFound(modelList[0])
