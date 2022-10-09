from python_helper import DateTimeHelper, ObjectHelper
from python_framework import StaticConverter

from constant import BalanceConstant


def overrideDefaultValues(instance):
    # instance.id = instance.id if ObjectHelper.isNone(instance.id) else int(instance.id)
    instance.value = StaticConverter.getValueOrDefault(instance.value if ObjectHelper.isNone(instance.value) else float(instance.value), BalanceConstant.DEFAULT_VALUE)
    return instance
