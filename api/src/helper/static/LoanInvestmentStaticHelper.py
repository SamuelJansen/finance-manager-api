from python_helper import ObjectHelper


def getUniqueOperationKeyList(investmentDtoList):
    return list(set([
        investmentDto.key
        for investmentDto in investmentDtoList
    ]))


def getReturnsAmountRange(returnsAmount):
    return range(1, returnsAmount + 1)


def parseReturnsAmount(enumName):
    if ObjectHelper.isNone(enumName):
        return 0
    return int(enumName.replace('LOAN_', '').replace('R', ''))
