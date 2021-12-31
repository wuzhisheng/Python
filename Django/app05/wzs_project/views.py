from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse,render,redirect
from wzs_project import models

#登录界面
def login(request):
    error_msg=""
    if request.method == "POST":
        # 如果你是POST请求，我就取出提交的数据，做登录判断
        email = request.POST.get("email",None)
        pwd = request.POST.get("pwd",None)
        print(email,pwd)
        # 做是否登录成功的判断
        if email == "wzs@qq.com" and pwd == "123":
        # 登录成功
        # 回复一个特殊的响应，这个响应会让用户的浏览器请求指定的url
            return redirect("https://www.luffycity.com")
        else:
            error_msg = "邮箱或密码错误"
    # 不是post请求就走下面这一句
    return render(request,"login.html",{"error":error_msg})

# def user_list(request):
#     # 去数据库中查询所有的用户
#     # 利用ORM这个工具去查询数据库，不用自己去查询
#     # 去数据库中查询所有的用户
#     ret = models.UserInfo.objects.all()
#     print (ret[0].id,ret[0].name)#打印列表字段
#     return render(request,"user_list.html",{"user_list":ret})

#展示出版社列表
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    return render(request, "publisher_list.html", {"publisher_list": ret})

# 添加新的出版社
def add_publisher(request):
    #如果是POST请求，我就取到用户填写的数据
    if request.method == "POST":
        new_name = request.POST.get("publisher_name")
        #通过ORM去数据库里新建一条记录
        models.Publisher.objects.create(name=new_name)
        #引导用户访问出版社列表页面，查看是否添加成功 --》跳转
        return redirect("/publisher_list/")
    #用户第一次来,我给他返回一个用来填写的HTML页面
    return  render(request,"add_publisher.html")
