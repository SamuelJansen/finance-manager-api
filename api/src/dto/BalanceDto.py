from converter.static import BalanceStaticConverter


class BalanceRequestDto:
    def __init__(self,
        key = None,
        userKey = None,
        label = None,
        value = None
    ):
        self.key = key
        self.userKey = userKey
        self.label = label
        self.value = value
        BalanceStaticConverter.overrideDefaultValues(self)


class BalanceResponseDto:
    def __init__(self,
        key = None,
        userKey = None,
        label = None,
        value = None
    ):
        self.key = key
        self.userKey = userKey
        self.label = label
        self.value = value
        BalanceStaticConverter.overrideDefaultValues(self)
