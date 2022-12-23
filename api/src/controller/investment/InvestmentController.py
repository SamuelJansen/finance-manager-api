from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from domain.SecurityContext import SecurityContext
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
        roleRequired=[SecurityContext.ADMIN, SecurityContext.FINANCES_ADMIN, SecurityContext.USER, SecurityContext.FINANCES_USER],
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
        roleRequired=[SecurityContext.ADMIN, SecurityContext.FINANCES_ADMIN, SecurityContext.USER, SecurityContext.FINANCES_USER],
        requestParamClass=[InvestmentDto.InvestmentQueryAllDto],
        responseClass=[[InvestmentDto.InvestmentResponseDto]]
    )
    def get(self, params=None):
        return self.service.investment.findAllByQuery(params), HttpStatus.OK
