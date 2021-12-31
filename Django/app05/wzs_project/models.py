from django.db import models

# Create your models here.

# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)  # 自增的ID主键
    # 创建一个varchar(64)的唯一的不为空的字段
    name = models.CharField(max_length=64, null=False, unique=True)