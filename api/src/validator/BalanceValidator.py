from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from dto import BalanceDto
from model import Balance


@Validator()
class BalanceValidator:

    @ValidatorMethod(requestClass=[Balance.Balance, float])
    def validateTransaction(self, model, value):
        if ObjectHelper.isNone(model) or ObjectHelper.isNone(value):
            raise GlobalException(logMessage=f'Invalid operation. Balance: {model}, value: {value}', status=HttpStatus.INTERNAL_SERVER_ERROR)
        if 0 > model.value + value:
            raise GlobalException(message=f'Not enought funds', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[str])
    def validateExistsByKey(self, key):
        if not self.service.balance.existsByKey(key):
            raise GlobalException(message=f'''Balance does not exists''', status=HttpStatus.BAD_REQUEST)

    @ValidatorMethod(requestClass=[[BalanceDto.BalanceRequestDto]])
    def validateCreateAll(self, dtoList):
        userData = self.validator.security.validateAuthorizationAll([dto.userKey for dto in dtoList])
        if self.service.balance.existsByLabelInAndUserKey([dto.label for dto in dtoList], userData.key):
            raise GlobalException(message=f'''At least one balance already exists''', status=HttpStatus.BAD_REQUEST)
        return userData

    @ValidatorMethod(requestClass=[BalanceDto.BalanceRequestDto])
    def validateCreate(self, dto):
        userData = self.validator.security.validateAuthorization(dto.userKey)
        if self.service.balance.existsByLabelInAndUserKey([dto.label], userData.key):
            raise GlobalException(message=f'''The {dto.label} balance already exists''', status=HttpStatus.BAD_REQUEST)
        return userData

    @ValidatorMethod(requestClass=[Balance.Balance])
    def validateDeletion(self, model):
        return self.validator.security.validateAuthorization(model.userKey)
