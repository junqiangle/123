from django.db import models


# Create your models here.
class User(models.Model):
    s_name = models.CharField(max_length=20)  # 用户名
    s_pwd = models.CharField(max_length=80)  # 用户密码
    s_email = models.CharField(max_length=30)  # 用户邮箱

    # s_addressee=models.CharField(max_length=20)#收件人

    class Meta:
        db_table = 'freshuser'  # 生鲜用户表


class UserInfo(models.Model):  # 收件人收件地址 和用户是一对多
    u_addr = models.CharField(max_length=80)  # 收件人地址
    u_zip_code = models.CharField(max_length=10)  # 收件人邮编
    u_name = models.CharField(max_length=20)  # 收件人名字
    u_phone = models.CharField(max_length=20)  # 收件人电话号码
    u = models.ForeignKey(User)

    class Meta:
        db_table = 'userinfo'  # 收件人信息
