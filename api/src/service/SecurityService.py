from python_helper import log
from python_framework import Service, ServiceMethod, AuditoryUtil, SecurityManager, Serializer, EnumItem

from domain import UserData
from enumeration.SecurityContext import SecurityContext


@Service()
class SecurityService:

    @ServiceMethod()
    def getUserData(self):
        userData = AuditoryUtil.safellyGetCurrentAthentication(securityClass=UserData.UserData, service=self)
        userData.key = AuditoryUtil.getAthenticationIdentity(service=self)
        userData.roleList = [
            SecurityContext.map(role)
            for role in SecurityManager.getContext(apiInstance=self.globals.api)
        ]
        log.prettyJson(self.getUserData, 'User data', Serializer.getObjectAsDictionary(userData), logLevel=log.STATUS)
        return userData

    @ServiceMethod()
    def isAdmin(self):
        return self.isAdminModel(self.getUserData())

    @ServiceMethod()
    def isUser(self):
        return self.isUserModel(self.getUserData())

    @ServiceMethod(requestClass=[UserData.UserData])
    def isAdminModel(self, userData):
        return self.containsRole(SecurityContext.ADMIN, userData)

    @ServiceMethod(requestClass=[UserData.UserData])
    def isUserModel(self, userData):
        return self.containsRole(SecurityContext.USER, userData)

    @ServiceMethod(requestClass=[EnumItem, UserData.UserData])
    def containsRole(self, role, userData):
        return role in userData.roleList
