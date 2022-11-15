from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import InvestmentDto

@Controller(
    url = '/investment/report',
    tag = 'Investment Report',
    description = 'Investment Report controller'
    , logRequest = True
    , logResponse = True
)
class InvestmentReportAllController:

    @ControllerMethod(url = '/all',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        responseClass=[[dict]]
    )
    def get(self):
        return [
            {
                'key': 'abc',
                'balance': 'PICPAY',
                'label': 'A Loan',
                'type': 'LOAN_12R',
                'value': 100,
                'risk': 'HIGHT',
                'returns': {
                    'expected':[
                        {
                            'transactionAt': 'string',
                            'value': -100
                        },
                        {
                            'transactionAt': 'string',
                            'value': 10
                        },
                        {
                            'transactionAt': 'string',
                            'value': 8
                        },
                        {
                            'transactionAt': 'string',
                            'value': 10
                        },
                        {
                            'transactionAt': 'string',
                            'value': 10
                        },
                        {
                            'transactionAt': 'string',
                            'value': 10
                        },
                        {
                            'transactionAt': 'string',
                            'value': 10
                        }
                    ],
                    'executed': [
                        {
                            'transactionAt': 'string',
                            'value': -100
                        },
                        {
                            'transactionAt': 'string',
                            'value': 15
                        },
                        {
                            'transactionAt': 'string',
                            'value': 12
                        },
                        {
                            'transactionAt': 'string',
                            'value': 13
                        }
                    ]
                }
            },
            {
                'key': 'abcd',
                'balance': 'PICPAY',
                'label': 'Another Loan',
                'type': 'LOAN_07R',
                'value': 200,
                'risk': 'MEDIUM',
                'returns': {
                    'expected': [
                        {
                            'transactionAt': 'string',
                            'value': -200
                        },
                        {
                            'transactionAt': 'string',
                            'value': 22
                        },
                        {
                            'transactionAt': 'string',
                            'value': 20
                        },
                        {
                            'transactionAt': 'string',
                            'value': 20
                        },
                        {
                            'transactionAt': 'string',
                            'value': 20
                        }
                    ],
                    'executed': [
                        {
                            'transactionAt': 'string',
                            'value': -200
                        },
                        {
                            'transactionAt': 'string',
                            'value': 24
                        },
                        {
                            'transactionAt': 'string',
                            'value': 26
                        },
                        {
                            'transactionAt': 'string',
                            'value': 26
                        }
                    ]
                }
            }
        ], HttpStatus.OK
