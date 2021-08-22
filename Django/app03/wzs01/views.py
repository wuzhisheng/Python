from django.shortcuts import render

# Create your views here.

from django.shortcuts import  HttpResponse,render,redirect

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