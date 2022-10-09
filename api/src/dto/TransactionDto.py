from converter.static import TransactionStaticConverter


class TransactionRequestDto:
    def __init__(self,
        key = None,
        operationKey = None,
        balanceKey = None,
        value = None,
        type = None,
        status = None,
        transactionAt = None
    ):
        self.key = key
        self.operationKey = operationKey
        self.balanceKey = balanceKey
        self.value = value
        self.type = type
        self.status = status
        self.transactionAt = transactionAt
        TransactionStaticConverter.overrideDefaultValues(self)


class TransactionResponseDto:
    def __init__(self,
        key = None,
        operationKey = None,
        balanceKey = None,
        value = None,
        type = None,
        status = None,
        transactionAt = None
    ):
        self.key = key
        self.operationKey = operationKey
        self.balanceKey = balanceKey
        self.value = value
        self.type = type
        self.status = status
        self.transactionAt = transactionAt
        TransactionStaticConverter.overrideDefaultValues(self)


class TransactionQueryDto:
    def __init__(self,
        key = None,
        operationKey = None,
        balanceKey = None,
        type = None,
        status = None,
        fromDateTime = None,
        toDateTime = None
    ):
        self.key = key
        self.operationKey = operationKey
        self.balanceKey = balanceKey
        self.type = type
        self.status = status
        self.fromDateTime = fromDateTime
        self.toDateTime = toDateTime


class ExecutableTransactionRequestDto:
    def __init__(self,
        key = None,
        value = None,
        transactionAt = None
    ):
        self.key = key
        self.value = value
        self.transactionAt = transactionAt
