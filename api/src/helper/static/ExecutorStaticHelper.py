from python_helper import ObjectHelper


def buildTransactionKey(transaction):
    if ObjectHelper.isNone(transaction.key):
        raise Exception(f'Cannot create transaction executable key. Transaction: {transaction}')
    return f'Transaction(key={transaction.key})'
