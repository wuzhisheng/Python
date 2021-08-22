
from django.shortcuts import  HttpResponse,render
def yimi(request):
    return HttpResponse('hello yimi')

# def xiaohei(requets):
#     #request参数保存了所有和用户浏览器请求相关的数据
#     with open("./templates/yimi.html","r",encoding="utf-8") as f:
#         data=f.read()
#     return HttpResponse(data)

def xiaohei(request):
    return render(request,"yimi.html")

def login(request):
    return render(request,"login.html")
