from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from model import Executable


@Validator()
class ExecutorValidator:

    @ValidatorMethod(requestClass=[Executable.Executable])
    def validateNotInProcess(self, model):
        if self.service.executor.exists(model):
            raise GlobalException(message=f'Operation being processed already', status=HttpStatus.BAD_REQUEST)
