from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from model import Balance


@Validator()
class BalanceValidator:

    @ValidatorMethod(requestClass=[Balance.Balance, float])
    def validateTransaction(self, model, value):
        if ObjectHelper.isNone(model) or ObjectHelper.isNone(value):
            raise GlobalException(logMessage=f'Invalid operation. Balance: {model}, value: {value}', status=HttpStatus.INTERNAL_SERVER_ERROR)
        if 0 > model.value + value:
            raise GlobalException(message=f'Not enought funds', status=HttpStatus.BAD_REQUEST)
