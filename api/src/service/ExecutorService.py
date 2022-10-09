from python_helper import ObjectHelper
from python_framework import Service, ServiceMethod

from model import Executable


@Service()
class ExecutorService:

    @ServiceMethod(requestClass=[Executable.Executable])
    def add(self, model):
        return self.repository.executor.add(model)

    @ServiceMethod(requestClass=[Executable.Executable])
    def remove(self, model):
        return self.repository.executor.remove(model)

    @ServiceMethod(requestClass=[Executable.Executable])
    def exists(self, model):
        return self.repository.executor.exists(model)

    @ServiceMethod(requestClass=[Executable.Executable])
    def validateNotInProcessAndAdd(self, model):
        self.validator.executor.validateNotInProcess(model)
        return self.repository.executor.add(model)

    @ServiceMethod(requestClass=[Executable.Executable])
    def removeIfNeeded(self, model):
        if self.repository.executor.exists(model):
            return self.repository.executor.remove(model)
        return model
