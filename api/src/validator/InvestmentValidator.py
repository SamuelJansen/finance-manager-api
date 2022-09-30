from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem

from model import Investment


@Validator()
class InvestmentValidator:

    @ValidatorMethod(requestClass=[Investment.Investment])
    def validateIsNotNone(self, model):
        if ObjectHelper.isNone(model):
            raise GlobalException(message=f'Investment not found', status=HttpStatus.NOT_FOUND)
