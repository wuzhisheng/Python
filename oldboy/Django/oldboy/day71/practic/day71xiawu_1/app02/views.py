from django.shortcuts import HttpResponse,render,redirect

# Create your views here.
from functools import wraps
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect

def check_login(func):
    @wraps(func) #装饰器修复技术：修复注释 文档
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        if ret == "1":
            # 已登录过就继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            #获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/app02/login/?next={}".format(next_url))
    return inner

def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        #从url 中渠道next参数
        next_url = request.GET.get("next")
        if user == "wzs" and pwd == "123":
            # 登陆成功
            # 告诉浏览器保存一个键值对
            if next_url:
                rep = redirect(next_url)  # 得到一个响应对象
            else:
                rep = redirect("/app02/home/")  # 得到一个响应对象
            request.session["is_login"] = "1"
            request.session["name"] = user  #获取登录名
            # request.session.set_expiry(7) #7秒钟失效
            return rep
    return render(request, "app02/login.html")

@check_login
def home(request):
    user = request.session.get("name")
    return render(request, "app02/home.html",{"user":user})

@check_login
def index(request):
    return render(request, "app02/index.html")

#注销函数

def logout(request):
    # 如何删除session
    request.session.flush()
    return redirect("/app02/login/")