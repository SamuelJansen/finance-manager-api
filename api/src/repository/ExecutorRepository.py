from python_framework import Repository
from model import Executable


@Repository(model = Executable.Executable)
class ExecutorRepository:

    __memmory__ = dict()

    def add(self, model):
        if self.exists(model):
            raise Exception(f'The "{model.key}" executable already exists')
        self.__memmory__[model.key] = model
        return model

    def remove(self, model):
        if not self.exists(model):
            raise Exception(f'The "{model.key}" executable does not exists')
        return self.__memmory__.pop(model.key)

    def exists(self, model):
        return model.key in self.__memmory__
