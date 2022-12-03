from python_helper import ObjectHelper
from python_framework import Validator, ValidatorMethod, GlobalException, HttpStatus

from domain import UserData


@Validator()
class SecurityValidator:

    @ValidatorMethod(requestClass=[[str]])
    def validateAuthorizationAll(self, userKeyList):
        userData = self.service.security.getUserData()
        for userKey in userKeyList:
            self._validateAuthorization(userKey, userData)
        return userData

    @ValidatorMethod(requestClass=[str])
    def validateAuthorization(self, userKey):
        return self.validateAuthorizationAll([userKey])

    @ValidatorMethod(requestClass=[str, UserData.UserData])
    def _validateAuthorization(self, userKey, userData):
        if ObjectHelper.isNone(userKey):
            raise GlobalException(message=f'''User key cannot be none''', status=HttpStatus.BAD_REQUEST)
        if not ObjectHelper.equals(userData.key, userKey):
            raise GlobalException(message=f'''Invalid user key''', status=HttpStatus.BAD_REQUEST)
