from django.shortcuts import HttpResponse,render,redirect

# Create your views here.
from functools import wraps

def check_login(func):
    @wraps(func) #装饰器修复技术：修复注释 文档
    def inner(request,*args,**kwargs):
        ret = request.get_signed_cookie("is_login",default="0",salt="s10nb")
        if ret == "1":
            # 已登录过就继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            #获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/app01/login/?next={}".format(next_url))
    return inner

def login(request):
    print(request.get_full_path())    #取绝对路径
    print(request.path_info)
    print("_"*120)
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        #从url 中渠道next参数
        next_url = request.GET.get("next")
        if user == "wzs" and pwd == "123":
            if next_url:
                rep = redirect(next_url)  # 得到一个响应对象
            else:
                rep = redirect("/app01/home/")  # 得到一个响应对象
            #rep.set_cookie(name,value)
            # rep.set_cookie("is_login","1")
            #设置加盐的cookie
            #salt="s10nb"  s10nb算法  将 value 加密
            #max_age=5 设置5s超时时间 5秒后刷新 返回登录页面
            rep.set_signed_cookie("is_login","1", salt="s10nb",max_age=10)
            return rep

    return render(request, "app01/login.html")

def home(request):
    #登录login py得到cookie键
    # ret = request.COOKIES["xiaohei"]
    # print(ret)
    # ret = request.COOKIES.get("is_login",0)
    #取加盐过的
    ret = request.get_signed_cookie("is_login",default="0",salt="s10nb")
    print(ret,type(ret))
    if ret == "1":
        return render(request, "app01/home.html")
    else:
        return redirect("app01/login/")

@check_login
def index(request):
    return render(request, "app01/index.html")

#注销函数
def logout(request):
    # 如何删除cookic
    rep = redirect("/app01/login/")
    rep.delete_cookie("is_login")
    return rep