
from django.shortcuts import  HttpResponse,render,redirect
def yimi(request):
    return HttpResponse('hello yimi')

# def xiaohei(requets):
#     #request参数保存了所有和用户浏览器请求相关的数据
#     with open("./templates/yimi.html","r",encoding="utf-8") as f:
#         data=f.read()
#     return HttpResponse(data)

def xiaohei(request):
    #request参数保存了所有和用户浏览器请求相关的数据
    return render(request,"yimi.html")

#方法一
# def login(request):
#     #如果你是GET请求
#     return render(request,"login.html")
#     #如果你是POST请求，我就取出提交的数据，做登录判断
# def baobao(request):
#     #获取用户提交的数据
#     # 取到所有POST的数据
#     # print(request.POST)
#     # return HttpResponse("WZS")
#     # print(request.POST)
#     email = request.POST.get("email",None)
#     pwd = request.POST.get("pwd", None)
#     print(email,pwd)
#     #做是否登录成功的判断
#     if email == "wzs@qq.com" and pwd == "123":
#         return HttpResponse("登录成功!")
#     else:
#         return HttpResponse("登录失败")



#方法二: POST和GET一起
# def login(request):
#     if request.method == "GET": #GET必须是大写
#     #如果你是GET请求
#         return render(request,"login.html")
#     #如果你是POST请求，我就取出提交的数据，做登录判断
#     else:
#         email = request.POST.get("email",None)
#         pwd = request.POST.get("pwd", None)
#         print(email,pwd)
#         #做是否登录成功的判断
#         if email == "wzs@qq.com" and pwd == "123":
#             return HttpResponse("登录成功!")
#         else:
#             # return HttpResponse("登录失败")
#             return render(request,"login.html")

#方法三 优化代码
# def login(request):
#     if request.method == "POST":
#     #如果你是POST请求，我就取出提交的数据，做登录判断
#         email = request.POST.get("email", None)
#         pwd = request.POST.get("pwd", None)
#         print(email, pwd)
#         # 做是否登录成功的判断
#         if email == "wzs@qq.com" and pwd == "123":
#             return HttpResponse("登录成功!")
#     #不是post请求就走下面这一句
#     return render(request,"login.html")

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