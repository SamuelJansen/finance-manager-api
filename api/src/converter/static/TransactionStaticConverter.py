from python_helper import DateTimeHelper, ObjectHelper
from python_framework import StaticConverter

from constant import TransactionConstant
from enumeration.TransactionType import TransactionType
from enumeration.TransactionStatus import TransactionStatus


def overrideDefaultValues(instance):
    # instance.id = instance.id if ObjectHelper.isNone(instance.id) else int(instance.id)
    instance.operationKey = StaticConverter.getValueOrDefault(instance.operationKey, TransactionConstant.DEFAULT_OPERATION_KEY)
    instance.value = StaticConverter.getValueOrDefault(instance.value if ObjectHelper.isNone(instance.value) else float(instance.value), TransactionConstant.DEFAULT_VALUE)
    instance.type = StaticConverter.getValueOrDefault(TransactionType.map(instance.type), TransactionConstant.DEFAULT_TYPE)
    instance.status = StaticConverter.getValueOrDefault(TransactionStatus.map(instance.status), TransactionConstant.DEFAULT_STATUS)
    instance.transactionAt = StaticConverter.getValueOrDefault(DateTimeHelper.of(dateTime=instance.transactionAt), DateTimeHelper.now())
    return instance
