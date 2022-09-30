from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import InvestmentDto

@Controller(
    url = '/investment',
    tag = 'Investment',
    description = 'Investment controller'
    # , logRequest = True
    # , logResponse = True
)
class InvestmentController:

    @ControllerMethod(
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[InvestmentDto.InvestmentResponseDto]
        # , logRequest = True
        # , logResponse = True
    )
    def get(self):
        return self.service.investment.findByKey(), HttpStatus.OK
