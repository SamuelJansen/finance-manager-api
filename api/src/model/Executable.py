from python_helper import ObjectHelper

class Executable:
    __tablename__ = 'Executable'

    def __init__(self,
        key = None,
        value = None
    ):
        self.key = key
        self.value = value

    def __eq__(self, obj):
        return ObjectHelper.isNotNone(self.key) and isinstance(obj, ObjectHelper.type(self)) and self.key == obj.key

    def __ne__(self, obj):
        return self.__eq__(obj)

    def __repr__(self):
        return f'{self.__tablename__}(key={self.key})'
