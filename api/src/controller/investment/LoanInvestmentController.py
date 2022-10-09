from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
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
        requestParamClass=[InvestmentDto.LoanInvestmentQueryRequestDto],
        responseClass=[InvestmentDto.LoanInvestmentResponseDto]
    )
    def get(self, params=None):
        return self.service.loanInvestment.findByQuery(params), HttpStatus.OK

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
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
        requestParamClass=[InvestmentDto.LoanInvestmentQueryAllRequestDto],
        responseClass=[[InvestmentDto.LoanInvestmentResponseDto]]
    )
    def get(self, params=None):
        return self.service.loanInvestment.findAllByQuery(params), HttpStatus.OK
