from python_helper import ObjectHelper


def getUniqueOperationKeyList(investmentDtoList):
    return list(set([
        investmentDto.key
        for investmentDto in investmentDtoList
    ]))


def getTotalReturnsRange(totalReturns):
    return range(1, totalReturns + 1)


def parseTotalReturns(enumName):
    if ObjectHelper.isNone(enumName):
        return 0
    return int(enumName.replace('LOAN_', '').replace('R', ''))
