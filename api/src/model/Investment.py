from python_helper import DateTimeHelper
from python_framework import StaticConverter, Serializer
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import INVESTMENT, MODEL
from constant import InvestmentConstant, ModelConstant
from converter.static import InvestmentStaticConverter


class Investment(MODEL):
    __tablename__ = INVESTMENT

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, unique=True)
    balanceKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    value = sap.Column(sap.Float(*ModelConstant.DEFAUTL_FLOAT_MONETARY_FORMAT), nullable=False, default=InvestmentConstant.DEFAULT_VALUE)
    expectedReturn = sap.Column(sap.Float(*ModelConstant.DEFAUTL_FLOAT_MONETARY_FORMAT), nullable=False, default=InvestmentConstant.DEFAULT_VALUE)
    risk = sap.Column(sap.Float(3, 2), nullable=False, default=InvestmentConstant.DEFAULT_VALUE)
    type = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, default=InvestmentConstant.DEFAULT_TYPE)
    status = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, default=InvestmentConstant.DEFAULT_STATUS)
    startAt = sap.Column(sap.DateTime(), nullable=False, default=DateTimeHelper.now())

    def __init__(self,
        id = None,
        key = None,
        balanceKey = None,
        value = None,
        expectedReturn = None,
        risk = None,
        type = None,
        status = None,
        startAt = None
    ):
        self.id = id
        self.key = StaticConverter.getValueOrDefault(key, Serializer.newUuidAsString())
        self.balanceKey = balanceKey
        self.value = value
        self.expectedReturn = expectedReturn
        self.risk = risk
        self.type = type
        self.status = status
        self.startAt = startAt
        self.reload()

    def __onChange__(self, *args, **kwargs):
        InvestmentStaticConverter.overrideDefaultValues(self)

    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, value={self.value}, type={self.type}, status={self.status}, startAt={self.startAt})'
