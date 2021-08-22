from django.db import models

# Create your models here.
# ORM相关的只能写在这个文件里,写到别的文件里Django找不到

#创建个Userinfo表
#若要删除则将该以下创建sql表语句 注释 即可
# 1. python3 manage.py makemigrations #app01/migrations文件下记录models.py文件变动语句
# 2. python3 manage.py migrate #将这些改动翻译成SQL语言并在数据库运行
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键字段
    name = models.CharField(null=False, max_length=30)   # 创建一个varchar(20)类型的不能为空的字段

    #<QuerySet [<UserInfo: UserInfo object (1)>, <UserInfo: UserInfo object (2)>, <UserInfo: UserInfo object (3)>]>
    def __str__(self):
        return "<{}-{}>".format(self.id, self.name)
    #<QuerySet [<UserInfo: <1-wu>>, <UserInfo: <2-zhi>>, <UserInfo: <3-sheng>>]>