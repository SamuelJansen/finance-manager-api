from converter.static import InvestmentStaticConverter


class InvestmentRequestDto:
    def __init__(self,
        key = None,
        userKey = None,
        balanceKey = None,
        value = None,
        expectedReturn = None,
        risk = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.value = value
        self.expectedReturn = expectedReturn
        self.risk = risk
        self.type = type
        self.status = status
        self.startAt = startAt
        InvestmentStaticConverter.overrideDefaultValues(self)


class InvestmentResponseDto:
    def __init__(self,
        key = None,
        userKey = None,
        balanceKey = None,
        value = None,
        expectedReturn = None,
        risk = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.value = value
        self.type = type
        self.expectedReturn = expectedReturn
        self.risk = risk
        self.status = status
        self.startAt = startAt
        InvestmentStaticConverter.overrideDefaultValues(self)


class LoanInvestmentRequestDto:
    def __init__(self,
        key = None,
        userKey = None,
        balanceKey = None,
        value = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.value = value
        self.type = type
        self.status = status
        self.startAt = startAt
        InvestmentStaticConverter.overrideDefaultValues(self)


class LoanInvestmentResponseDto:
    def __init__(self,
        key = None,
        userKey = None,
        balanceKey = None,
        value = None,
        type = None,
        expectedReturn = None,
        risk = None,
        status = None,
        startAt = None,
        transactionList = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.value = value
        self.type = type
        self.expectedReturn = expectedReturn
        self.risk = risk
        self.status = status
        self.startAt = startAt
        self.transactionList = transactionList
        InvestmentStaticConverter.overrideDefaultValues(self)


class LoanInvestmentQueryRequestDto:
    def __init__(self,
        key = None,
        userKey = None
    ):
        self.key = key
        self.userKey = userKey
        InvestmentStaticConverter.overrideDefaultQueryValues(self)


class LoanInvestmentQueryAllRequestDto:
    def __init__(self,
        userKey = None,
        keyList = None
    ):
        self.userKey = userKey
        self.keyList = keyList
        InvestmentStaticConverter.overrideDefaultQueryValues(self)
