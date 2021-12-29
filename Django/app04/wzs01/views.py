from django.shortcuts import HttpResponse,render,redirect

# Create your views here.
#专门来放函数

from django.shortcuts import  HttpResponse,render,redirect
from wzs01 import models

#进程4
def login(request):
    error_msg = ""
    if request.method == "POST":
    #如果你是POST请求，我就取出提交的数据，做登录判断
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        # 做是否登录成功的判断
        if email == "wzs@qq.com" and pwd == "123":
            #登录成功
            #回复一个特殊的响应，这个响应会让用户的浏览器请求指定的url
            return redirect("https://www.luffycity.com")
        else:
            #登录失败
            error_msg = "邮箱或密码错误"
    #不是post请求就走下面这一句
    return render(request,"login.html",{"error":error_msg})

#展示所有的用户的函数
def user_list(request):
	#去数据库中查询所有的用户
	#利用ORM这个工具去查询数据库，不用自己去查询
    #去数据库中查询所有的用户
    ret = models.UserInfo.objects.all()#【UserInfo object UserInfo object 】
    # 显示<QuerySet [<UserInfo: UserInfo object (1)>, <UserInfo: UserInfo object (2)>]>
    print (ret[0].id,ret[0].name) #打印列表字段
   # return HttpResponse("别哭了！")
    #打开user_list
    return render(request,"user_list.html",{"user_list":ret}) #做ret字符串替换