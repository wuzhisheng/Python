from django.shortcuts import HttpResponse, render,redirect
#Django三剑客
    #HttpResponse 返回html字符串
    #render返回完整htmk文件
    #redirect 跳转


def yimi(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    #方法一
    # with open("templates/xxx/yimi.html", "r", encoding="utf-8") as f:
    #     data = f.read()
    # return HttpResponse(data)
    #方法二
    return render(request, "xxx/yimi.html")

def xiaohei(request):
    # request参数保存了所有和用户浏览器请求相关的数据
    return HttpResponse('hello xiaohei! haha 小黑真黑啊!')

#GET请求和POST请求分开情况
# def login(request):
#     return render(request, "login.html")

#
# def baobao(request):
#     # 获取用户提交的数据
#     # print(request.POST)
#     email=request.POST.get("email",None)
#     pwd=request.POST.get("pwd",None)
#     print(email,pwd)
#     # 做是否登录成功的判断
#     if email == "alex@oldboyedu.com" and pwd == "alexdsb":
#         return HttpResponse('登录成功')
#     else:
#         return HttpResponse('登录失败')

#登录方法一
# def login(request):
#     #如果是GET请求
#     if request.method == "GET":
#         return render(request, "login.html")
#     #如果是POST请求，我就取出提交的数据，做出登录判断
#     else:
#         email=request.POST.get("email",None)
#         pwd=request.POST.get("pwd",None)
#         print(email,pwd)
#         # 做是否登录成功的判断
#         if email == "alex@oldboyedu.com" and pwd == "alexdsb":
#             return HttpResponse('登录成功')
#         else:
#             #登录失败返回登录界面
#             return render(request, "login.html")


#登录方法二：优化
# def login(request):
#     if request.method == "POST":
#         email = request.POST.get("email", None)
#         pwd = request.POST.get("pwd", None)
#         print(email, pwd)
#         # 做是否登录成功的判断
#         if email == "alex@oldboyedu.com" and pwd == "alexdsb":
#             return HttpResponse('登录成功')
#     #不是POST请求就走下面这一句
#     return render(request, "login.html")

def login(request):
    error_msg=""
    if request.method == "POST":
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print(email, pwd)
        # 做是否登录成功的判断
        if email == "alex@oldboyedu.com" and pwd == "alexdsb":
            return HttpResponse('登录成功')
            #回复一个特殊的响应，这个响应会让用户的浏览器请求指定的URL
            # return credits("http://www.baidu.com")
        else:
            error_msg="邮箱或密码错误"
    #不是POST请求就走下面这一句
    return render(request, "login.html",{"error":error_msg})