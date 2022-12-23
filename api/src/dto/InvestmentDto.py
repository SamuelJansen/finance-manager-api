from converter.static import InvestmentStaticConverter


class InvestmentRequestDto:
    def __init__(self,
        key = None,
        userKey = None,
        balanceKey = None,
        label = None,
        value = None,
        # expectedReturn = None,
        # executedReturn = None,
        risk = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.label = label
        self.value = value
        # self.expectedReturn = expectedReturn
        # self.executedReturn = executedReturn
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
        label = None,
        value = None,
        # expectedReturn = None,
        # executedReturn = None,
        risk = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.label = label
        self.value = value
        self.type = type
        # self.expectedReturn = expectedReturn
        # self.executedReturn = executedReturn
        self.risk = risk
        self.status = status
        self.startAt = startAt
        InvestmentStaticConverter.overrideDefaultValues(self)


class InvestmentQueryAllDto:
    def __init__(self,
        userKey = None,
        keyList = None,
        labelList = None,
        typeList = None
    ):
        self.userKey = userKey
        self.keyList = keyList
        self.labelList = labelList
        self.typeList = typeList


class LoanInvestmentRequestDto:
    def __init__(self,
        key = None,
        userKey = None,
        balanceKey = None,
        label = None,
        value = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.label = label
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
        label = None,
        value = None,
        type = None,
        # expectedReturn = None,
        # executedReturn = None,
        risk = None,
        status = None,
        startAt = None,
        transactionList = None
    ):
        self.key = key
        self.userKey = userKey
        self.balanceKey = balanceKey
        self.label = label
        self.value = value
        self.type = type
        # self.expectedReturn = expectedReturn
        # self.executedReturn = executedReturn
        self.risk = risk
        self.status = status
        self.startAt = startAt
        self.transactionList = transactionList
        InvestmentStaticConverter.overrideDefaultValues(self)


class LoanInvestmentQueryDto:
    def __init__(self,
        key = None,
        userKey = None,
        label = None
    ):
        self.key = key
        self.userKey = userKey
        self.label = label
        InvestmentStaticConverter.overrideDefaultQueryValues(self)


class LoanInvestmentQueryAllDto:
    def __init__(self,
        userKey = None,
        keyList = None,
        labelList = None
    ):
        self.userKey = userKey
        self.keyList = keyList
        self.labelList = labelList
        InvestmentStaticConverter.overrideDefaultQueryValues(self)
