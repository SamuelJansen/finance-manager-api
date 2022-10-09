from converter.static import BalanceStaticConverter


class BalanceRequestDto:
    def __init__(self,
        key = None,
        value = None
    ):
        self.key = key
        self.value = value
        BalanceStaticConverter.overrideDefaultValues(self)


class BalanceResponseDto:
    def __init__(self,
        key = None,
        value = None
    ):
        self.key = key
        self.value = value
        BalanceStaticConverter.overrideDefaultValues(self)
