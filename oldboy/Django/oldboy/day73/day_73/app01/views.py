from django.shortcuts import render
import json
# Create your views here.

def reg(request):
    error = {"pwd":"" ,"user":""}
    if request.method == "POST":
        name = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if len(pwd) < 6:
            error["pwd"] = "密码不能小于6位"
    return render(request, "reg.html" ,{"error":error})


# Django Form组件的使用
#from自动生成HTML
from django import forms
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class RegForm(forms.Form):
    name = forms.CharField(max_length=16,label="用户名")
    pwd = forms.CharField(label="密码",
                          min_length=6,
                          max_length=24,
                          widget=widgets.PasswordInput(),
                          error_messages={
                              "min_length":"密码不能少于6位！",
                              "max_length":"密码最长不能大于24位！",
                          }
                          )

    re_pwd = forms.CharField(
        label="确认密码",
        min_length=6,
        max_length=10,
        widget=widgets.PasswordInput(attrs={"class": "form-control"}, render_value=True),
        error_messages={
            "min_length": "密码不能少于6位！",
            "max_length": "密码最长10位！",
            "required": "该字段不能为空",
        }
    )

    email = forms.EmailField(
        label="邮箱",

        widget=widgets.EmailInput(attrs={"class": "form-control"}),
        error_messages={
            "required": "该字段不能为空",
        }
    )

    gender = forms.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect
    )

    hobby = forms.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )

    hobby1 = forms.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )

    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )

    hobby3 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple(attrs={"class": "c1"}),
    )

def reg2(request):
    form_obj = RegForm()
    if request.method == "POST":
        form_obj = RegForm(request.POST)
        #让form 帮我们做检验
    if form_obj.is_valid():
        pass
    return render(request,"reg2.html",{"form_obj":form_obj})