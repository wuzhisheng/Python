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

#添加用户
def add_user(request):
    if request.method == "POST":
        #用户填写了新的用户名，并发送了POST请求过来
        new_name = request.POST.get("username",None)
        #去数据库中新创建一条用户记录
        models.UserInfo.objects.create(name=new_name)
        #return HttpResponse("添加成功")
        #添加成功后直接跳转到用户列表页
        #跳到自己网站 只需要添加相对路径
        return  redirect("/user_list/")
    #第一次请求页面的时候，就返回一个页面，页面上有两个框让用户填写
    return render(request,"add_user.html")

#展示出版社列表
def publisher_list(request):
    ret = models.UserInfo.objects.all().order_by("id")
    # return render(request,"publisher_list.html",{"publisher_list":ret})
    return render(request, "publisher_list.html", {"publisher_list": ret})