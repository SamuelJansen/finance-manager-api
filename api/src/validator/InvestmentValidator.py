from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus, EnumItem

from dto import InvestmentDto
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


    @ValidatorMethod(requestClass=[InvestmentDto.InvestmentQueryAllDto])
    def validateFindAllByQuery(self, queryDto):
        return self.validator.security.validateAuthorization(queryDto.userKey)


    @ValidatorMethod(requestClass=[[InvestmentDto.InvestmentRequestDto]])
    def validateCreateAll(self, dtoList):
        userData = self.validator.security.validateAuthorizationAll([dto.userKey for dto in dtoList])
        if self.service.investment.existsByLabelInAndUserKey([dto.label for dto in dtoList], userData.key):
            raise GlobalException(message=f'''At least one investment already exists''', status=HttpStatus.BAD_REQUEST)
        return userData


    @ValidatorMethod(requestClass=[InvestmentDto.InvestmentRequestDto])
    def validateCreate(self, dto):
        userData = self.validator.security.validateAuthorization(dto.userKey)
        if self.service.investment.existsByLabelInAndUserKey([dto.label], userData.key):
            raise GlobalException(message=f'''The {dto.label} investment already exists''', status=HttpStatus.BAD_REQUEST)
        return userData


    @ValidatorMethod(requestClass=[Investment.Investment])
    def validateDeletion(self, model):
        return self.validator.security.validateAuthorization(model.userKey)
