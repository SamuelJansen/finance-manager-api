from python_helper import DateTimeHelper, ObjectHelper, ReflectionHelper
from python_framework import StaticConverter, Serializer

from constant import InvestmentConstant
from enumeration.InvestmentType import InvestmentType
from enumeration.InvestmentStatus import InvestmentStatus


def overrideDefaultValues(instance, objectKeys=None):
    # instance.id = instance.id if ObjectHelper.isNone(instance.id) else int(instance.id)
    if ObjectHelper.isNone(instance):
        return instance
    # objectKeys = [key for key in [*instance.__dir__()] if ReflectionHelper.isAttributeName(key, instance)]
    objectKeys = StaticConverter.getValueOrDefault(objectKeys, ReflectionHelper.getAttributeNameListFromInstance(instance))
    if 'value' in objectKeys:
        instance.value = StaticConverter.getValueOrDefault(instance.value if ObjectHelper.isNone(instance.value) else float(instance.value), InvestmentConstant.DEFAULT_VALUE)
    if 'expectedReturn' in objectKeys:
        instance.expectedReturn = StaticConverter.getValueOrDefault(instance.expectedReturn if ObjectHelper.isNone(instance.expectedReturn) else float(instance.expectedReturn), InvestmentConstant.DEFAULT_EXPECTED_RETURN)
    if 'risk' in objectKeys:
        instance.risk = StaticConverter.getValueOrDefault(instance.risk if ObjectHelper.isNone(instance.risk) else float(instance.risk), InvestmentConstant.DEFAULT_PERCENTUAL_RISK)

    if 'type' in objectKeys:
        instance.type = StaticConverter.getValueOrDefault(InvestmentType.map(instance.type), InvestmentConstant.DEFAULT_TYPE)
    if 'status' in objectKeys:
        instance.status = StaticConverter.getValueOrDefault(InvestmentStatus.map(instance.status), InvestmentConstant.DEFAULT_STATUS)
    if 'startAt' in objectKeys:
        instance.startAt = StaticConverter.getValueOrDefault(DateTimeHelper.of(dateTime=instance.startAt), DateTimeHelper.now())
    return instance

def overrideDefaultQueryValues(instance, objectKeys=None):
    if ObjectHelper.isNone(instance):
        return instance
    objectKeys = StaticConverter.getValueOrDefault(objectKeys, ReflectionHelper.getAttributeNameListFromInstance(instance))
    overrideDefaultValues(instance, objectKeys=objectKeys)
    if 'keyList' in objectKeys:
        instance.keyList = StaticConverter.getValueOrDefault(instance.keyList, [])
    return instance
