from python_helper import log
from python_framework import Service, ServiceMethod, AuditoryUtil, SecurityManager, Serializer, EnumItem, StaticConverter, JwtConstant

from domain import UserData
from domain.SecurityContext import SecurityContext


@Service()
class SecurityService:

    @ServiceMethod()
    def getUserData(self):
        userData = AuditoryUtil.safellyGetCurrentAthentication(securityClass=UserData.UserData, service=self)
        userData.key = StaticConverter.getValueOrDefault(
            userData.key,
            userData._contextInfo.get(JwtConstant.KW_IDENTITY)
        )
        securityContextItemsAsString = SecurityContext.getItemsAsString()
        userData.roles = [
            SecurityContext.map(role)
            for role in StaticConverter.getValueOrDefault(
                userData.roles,
                userData._contextInfo.get(JwtConstant.KW_CONTEXT)
            )
            if role in securityContextItemsAsString
        ]
        log.prettyJson(self.getUserData, 'User data', Serializer.getObjectAsDictionary(userData), logLevel=log.STATUS)
        return userData

    @ServiceMethod()
    def isAdmin(self):
        return self.isAdminDomain(self.getUserData())

    @ServiceMethod()
    def isUser(self):
        return self.isUserDomain(self.getUserData())

    @ServiceMethod(requestClass=[UserData.UserData])
    def isAdminDomain(self, userData):
        return self.containsRole(SecurityContext.FINANCES_ADMIN, userData)

    @ServiceMethod(requestClass=[UserData.UserData])
    def isUserDomain(self, userData):
        return self.containsRole(SecurityContext.FINANCES_USER, userData)

    @ServiceMethod(requestClass=[EnumItem, UserData.UserData])
    def containsRole(self, role, userData):
        return role in userData.roles
