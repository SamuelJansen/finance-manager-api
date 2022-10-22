from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import BalanceDto

@Controller(
    url = '/balance',
    tag = 'Balance',
    description = 'Balance controller'
    , logRequest = True
    , logResponse = True
)
class BalanceController:

    @ControllerMethod(url = '/<string:key>',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[]
    )
    def delete(self, key=None):
        return self.service.balance.deleteByKey(key), HttpStatus.OK


@Controller(
    url = '/balance',
    tag = 'Balance',
    description = 'Balance controller'
    , logRequest = True
    , logResponse = True
)
class BalanceAllController:

    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[[BalanceDto.BalanceResponseDto]]
    )
    def get(self):
        return self.service.balance.findAll(), HttpStatus.OK


    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestClass=[[BalanceDto.BalanceRequestDto]],
        responseClass=[[BalanceDto.BalanceResponseDto]]
    )
    def post(self, dtoList):
        return self.service.balance.createAll(dtoList), HttpStatus.CREATED
