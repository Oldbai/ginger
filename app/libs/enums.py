from enum import Enum


class ClientTypeEnum(Enum):
    # 通过邮箱
    USER_EMAIL = 100
    # 通过手机号
    USER_MOBILE = 101

    # 通过小程序
    USER_MINA = 200
    # 通过微信
    USER_WX = 201
