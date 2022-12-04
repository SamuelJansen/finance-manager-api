from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from domain.SecurityContext import SecurityContext
from dto import InvestmentDto

@Controller(
    url = '/investment/loan',
    tag = 'Investment Loan',
    description = 'Investment controller'
    , logRequest = True
    , logResponse = True
)
class LoanInvestmentController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.USER],
        requestParamClass=[InvestmentDto.LoanInvestmentQueryDto],
        responseClass=[InvestmentDto.LoanInvestmentResponseDto]
    )
    def get(self, params=None):
        return self.service.loanInvestment.findByQuery(params), HttpStatus.OK

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.USER],
        requestClass=[InvestmentDto.LoanInvestmentRequestDto],
        responseClass=[InvestmentDto.LoanInvestmentResponseDto]
    )
    def post(self, dto):
        return self.service.loanInvestment.create(dto), HttpStatus.CREATED


@Controller(
    url = '/investment/loan',
    tag = 'Investment Loan',
    description = 'Investment controller'
    , logRequest = True
    , logResponse = True
)
class LoanInvestmentAllController:

    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        roleRequired=[SecurityContext.ADMIN, SecurityContext.USER],
        requestParamClass=[InvestmentDto.LoanInvestmentQueryAllDto],
        responseClass=[[InvestmentDto.LoanInvestmentResponseDto]]
    )
    def get(self, params=None):
        return self.service.loanInvestment.findAllByQuery(params), HttpStatus.OK
