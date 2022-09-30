from python_framework import ConverterStatic
from python_framework import SqlAlchemyProxy as sap

from ModelAssociation import INVESTMENT, MODEL
from constant import InvestmentConstant
from enumeration.InvestmentType import InvestmentType


class Investment(MODEL):
    __tablename__ = INVESTMENT

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    # key = sap.Column(sap.Investment, nullable=False, unique=True)
    # type = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False, default=InvestmentConstant.DEFAULT_TYPE)


    def __init__(self,
        id = None
        # key = None,
        # type = None
    ):
        self.id = id
        # self.key = key
        # self.type = type

    def __onChange__(self, *args, **kwargs):
        # self.key = InvestmentTimeHelper.dateOf(dateTime=InvestmentTimeHelper.of(date=self.key))
        # self.type = ConverterStatic.getValueOrDefault(InvestmentType.map(self.type), InvestmentConstant.DEFAULT_TYPE)
        return self

    def onChange(self, *args, **kwargs):
        return self.__onChange__(*args, **kwargs)

    # def __repr__(self):
    #     return f'{self.__tablename__}(id={self.id}, key={self.key}, type={self.type})'
