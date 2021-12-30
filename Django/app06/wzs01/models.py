from django.db import models

# Create your models here.
#ORM相关的只能写在这个里，写到别的文件里Django找不到
class UserInfo(models.Model):
    #创建一个自增的主键字段
    id = models.AutoField(primary_key=True)
    #创建一个carchar类型的不能为空的字段
    name = models.CharField(null=False,max_length=20)

#出版社
# class Publisher(models.Model):
#     id = models.AutoField(primary_key=True) #自增的ID主键
#     #创建一个varchar(64)的唯一的不为空的字段
#     name = models.CharField(max_length=64,null=False,unique=True)