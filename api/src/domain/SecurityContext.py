from python_framework import Enum, EnumItem


@Enum()
class SecurityContextEnumeration:
    USER = EnumItem()
    ADMIN = EnumItem()


SecurityContext = SecurityContextEnumeration()
