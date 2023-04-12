"""常量配置表"""

from enum import Enum

class UserStatus(Enum):
    """用户状态"""
    USER_ACTIVE=1#可登录
    USER_IN_ACTIVE = 0#不可登录

class UserRole(Enum):
    """用户角色"""
    COMMON=0#普通
    ADMIN = 1#普通管理员
    SUPER_ADMIN=2#超级管理员
