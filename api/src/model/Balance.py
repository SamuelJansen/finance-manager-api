from python_framework import StaticConverter, Serializer
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import BALANCE, MODEL
from constant import BalanceConstant, ModelConstant
from converter.static import BalanceStaticConverter


class Balance(MODEL):
    __tablename__ = BALANCE

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False, unique=True)
    userKey = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    label = sap.Column(sap.String(sap.MEDIUM_STRING_SIZE), nullable=False)
    value = sap.Column(sap.Float(*ModelConstant.DEFAUTL_FLOAT_MONETARY_FORMAT), nullable=False, default=BalanceConstant.DEFAULT_VALUE)

    def __init__(self,
        id = None,
        key = None,
        userKey = None,
        label = None,
        value = None
    ):
        self.id = id
        self.key = StaticConverter.getValueOrDefault(key, Serializer.newUuidAsString())
        self.userKey = userKey
        self.label = label
        self.value = value
        self.setDefaultValues()

    def __onChange__(self, *args, **kwargs):
        BalanceStaticConverter.overrideDefaultValues(self)
        return self

    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, label={self.label}, value={self.value})'
