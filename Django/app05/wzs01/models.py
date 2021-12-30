from django.db import models

# Create your models here.
# 图书管理系统, 书  作者 出版社

# 出版社
# class Publisher(models.Model):
#     id = models.AutoField(primary_key=True)  # 自增的ID主键
#     # 创建一个varchar(64)的唯一的不为空的字段
#     name = models.CharField(max_length=64, null=False, unique=True)

class Book(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    title = models.CharField(max_length=32) # 书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2) # 书籍价格
    publish = models.CharField(max_length=32) # 出版社名称
    pub_date = models.DateField() # 出版时间