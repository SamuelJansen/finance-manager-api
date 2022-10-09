from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import InvestmentDto

@Controller(
    url = '/investment',
    tag = 'Investment',
    description = 'Investment controller'
    , logRequest = True
    , logResponse = True
)
class InvestmentController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestClass=[InvestmentDto.InvestmentRequestDto],
        responseClass=[InvestmentDto.InvestmentResponseDto]
    )
    def post(self, dto):
        return self.service.investment.create(dto), HttpStatus.CREATED


@Controller(
    url = '/investment',
    tag = 'Investment',
    description = 'Investment controller'
    , logRequest = True
    , logResponse = True
)
class InvestmentAllController:

    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[[InvestmentDto.InvestmentResponseDto]]
    )
    def get(self):
        return self.service.investment.findAll(), HttpStatus.OK
