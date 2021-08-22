from django.shortcuts import HttpResponse,render,redirect

# Create your views here.

def index(request):
    return render(request,"index.html")


def ajax_add3(request):
    print(request.POST)
    i1 = request.POST.get("i1")
    i2 = request.POST.get("i2")
    i1 = int(i1)
    i2 = int(i2)
    ret = i1 + i2
    return HttpResponse(ret)

from app01 import models
def persons(request):
    ret = models.Person.objects.all()
    print(ret.values_list())
    # person_list = []
    # for i in ret:
    #     person_list.append({"name":i.name,"age":i.age})
    # print(person_list)
    # import json
    # s = json.dumps(person_list)
    # print(s)

    # from django.core import serializers
    # s = serializers.serialize("json",ret)
    # print(s)
    # return HttpResponse(s)

    return render(request,"sweetalert.html",{"persons":ret})

def delete(request):
    del_id = request.POST.get("id")
    models.Person.objects.filter(id=del_id).delete()
    return HttpResponse("删除成功！")





    
    