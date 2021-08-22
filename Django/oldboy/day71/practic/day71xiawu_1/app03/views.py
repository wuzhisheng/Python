from django.shortcuts import HttpResponse,render,redirect
from .models import UserInfo
# Create your views here.

def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # user_obj = UserInfo.objects.filter(name=user,pwd=pwd).first()
        # if user_obj:
        if user == "wzs" and pwd == "123":
            obj= HttpResponse("登录成功")
            obj.set_cookie("is_login",True)
            obj.set_cookie("username",user)
            return obj
    return render(request, "app03/login.html")

def index(request):
    print("COOKIES",request.COOKIES)
    is_login = request.COOKIES.get("is_login")
    if not is_login:
        return redirect("/app03/login/")
    return render(request,"app03/index.html")
