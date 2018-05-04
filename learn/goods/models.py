from django.db import models
from tinymce.models import HTMLField  # 导入富文本编辑器


# Create your models here.
class Goods(models.Model):
    t_title = models.CharField(max_length=20)  # 设计商品类型
    isDelete = models.BooleanField(default=False)  # 逻辑默认不删除

    class Meta:
        db_table = 'goods'


class GoodsInfo(models.Model):  # 商品类与商品是一对多
    g_title = models.CharField(max_length=40)  # 设计商品名称
    g_img = models.ImageField(upload_to='img_goods')  # 设计商品图片保存目录
    g_price = models.DecimalField(max_digits=5, decimal_places=2)  # max_digits  最大位数  decimal_places小数位数
    g_delete = models.BooleanField(default=False)  # 逻辑删除  默认 不删除
    g_unit = models.CharField(max_length=20, default='500g')  # 商品重量 默认500g
    g_click = models.ImageField()  # 点击量
    g_abstract = models.CharField(max_length=200)  # 商品简介
    g_inventory = models.ImageField()  # 库存还有多少
    g_content = HTMLField  # 商品详情介绍
    g = models.ForeignKey(Goods)  # 商品类外键
    # g_adv=models.BooleanField(default=False)# 重点推荐商品广告位

    class Meta:
        db_table = 'goods_info'
