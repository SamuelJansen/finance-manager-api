from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from domain.SecurityContext import SecurityContext
from dto import TransactionDto

@Controller(
    url = '/transaction',
    tag = 'Transaction',
    description = 'Transaction controller'
    , logRequest = True
    , logResponse = True
)
class TransactionController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.FINANCES_ADMIN],
        requestClass=[TransactionDto.TransactionRequestDto],
        responseClass=[TransactionDto.TransactionResponseDto]
    )
    def post(self, dto):
        return self.service.transaction.create(dto), HttpStatus.CREATED


    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.FINANCES_ADMIN],
        requestParamClass=[TransactionDto.TransactionQueryDto],
        responseClass=[TransactionDto.TransactionResponseDto]
    )
    def get(self, params=None):
        return self.service.transaction.findByQuery(params), HttpStatus.OK


@Controller(
    url = '/transaction',
    tag = 'Transaction',
    description = 'Transaction controller'
    , logRequest = True
    , logResponse = True
)
class TransactionAllController:

    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.FINANCES_ADMIN],
        requestClass=[[TransactionDto.TransactionRequestDto]],
        responseClass=[[TransactionDto.TransactionResponseDto]]
    )
    def post(self, dtoList):
        return self.service.transaction.createAll(dtoList), HttpStatus.CREATED


    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.FINANCES_ADMIN],
        requestParamClass=[TransactionDto.TransactionQueryDto],
        responseClass=[[TransactionDto.TransactionResponseDto]]
    )
    def get(self, params=None):
        return self.service.transaction.findAllByQuery(params), HttpStatus.OK
