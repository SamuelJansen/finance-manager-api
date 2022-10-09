from python_helper import DateTimeHelper
from python_framework import StaticConverter, Serializer
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import TRANSACTION, MODEL
from constant import TransactionConstant, ModelConstant
from converter.static import TransactionStaticConverter


class Transaction(MODEL):
    __tablename__ = TRANSACTION

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, unique=True)
    operationKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    balanceKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    value = sap.Column(sap.Float(*ModelConstant.DEFAUTL_FLOAT_MONETARY_FORMAT), nullable=False, default=TransactionConstant.DEFAULT_VALUE)
    type = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, default=TransactionConstant.DEFAULT_TYPE)
    status = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, default=TransactionConstant.DEFAULT_STATUS)
    transactionAt = sap.Column(sap.Integer(), nullable=False, default=DateTimeHelper.now())

    def __init__(self,
        id = None,
        key = None,
        operationKey = None,
        balanceKey = None,
        value = None,
        type = None,
        status = None,
        transactionAt = None
    ):
        self.id = id
        self.key = StaticConverter.getValueOrDefault(key, Serializer.newUuidAsString())
        self.operationKey = operationKey
        self.balanceKey = balanceKey
        self.value = value
        self.type = type
        self.status = status
        self.transactionAt = transactionAt
        self.reload()

    def __onChange__(self, *args, **kwargs):
        TransactionStaticConverter.overrideDefaultValues(self)

    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, key={self.key}, value={self.value}, type={self.type}, status={self.status}, transactionAt={self.transactionAt})'
