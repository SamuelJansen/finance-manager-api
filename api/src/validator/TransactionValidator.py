from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem

from dto import TransactionDto
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
    def validateIsCreated(self, modelList):
        if not 1 == len(modelList):
            raise GlobalException(logMessage=f'Transaction not created', status=HttpStatus.INTERNAL_SERVER_ERROR)


    @ValidatorMethod(requestClass=[[Transaction.Transaction]])
    def validateOnlyOneWasFound(self, modelList):
        if 0 == len(modelList):
            raise GlobalException(message=f'Transaction not found', status=HttpStatus.BAD_REQUEST)
        elif 1 < len(modelList):
            raise GlobalException(message=f'Multiple transactions were found. Please, refine your query', status=HttpStatus.BAD_REQUEST)
        self.validateIsFound(modelList[0])


    @ValidatorMethod(requestClass=[str])
    def validateExistsByKey(self, key):
        if not self.service.transaction.existsByKey(key):
            raise GlobalException(message=f'''Transaction does not exists''', status=HttpStatus.BAD_REQUEST)


    @ValidatorMethod(requestClass=[TransactionDto.TransactionQueryDto])
    def validateFindAllByQuery(self, queryDto):
        return self.validator.security.validateAuthorization(queryDto.userKey)


    @ValidatorMethod(requestClass=[[TransactionDto.TransactionRequestDto]])
    def validateCreateAll(self, dtoList):
        return self.validator.security.validateAuthorizationAll([dto.userKey for dto in dtoList])


    @ValidatorMethod(requestClass=[TransactionDto.TransactionRequestDto])
    def validateCreate(self, dto):
        return self.validator.security.validateAuthorization(dto.userKey)


    @ValidatorMethod(requestClass=[Transaction.Transaction])
    def validateDeletion(self, model):
        return self.validator.security.validateAuthorization(model.userKey)


    @ValidatorMethod(requestClass=[TransactionDto.ExecutableTransactionRequestDto])
    def validateExecution(self, dto):
        return self.validator.security.validateAuthorization(dto.userKey)
