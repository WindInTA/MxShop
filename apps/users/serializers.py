#!/usr/bin/env python
# @Time : 2019/1/30 4:55
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework import serializers
import re
from MxShop.settings import REGEX_MOBILE
from .models import VerifyCode

__author__ = 'Boaz'

User = get_user_model()

class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param mobile: 手机号码
        :return:
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE,mobile):
            raise serializers.ValidationError("手机号码不正确")

        # 验证发送频率
        one_minute_ago = datetime.now()-timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_minute_ago, mobile=mobile):
            raise serializers.ValidationError("距离上次发送未超过60秒")

        return mobile
