from python_framework import Enum, EnumItem


@Enum()
class SecurityContextEnumeration:
    ADMIN = EnumItem()
    FINANCES_ADMIN = EnumItem()

    USER = EnumItem()
    FINANCES_USER = EnumItem()


SecurityContext = SecurityContextEnumeration()
