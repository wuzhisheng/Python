from django.shortcuts import HttpResponse,render,redirect
from app01 import models
from functools import wraps
# Create your views here.
# session验证
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
            return redirect("/login/")
    return inner

def login(request):
    error_msg = ""
    if request.method == "POST":
        email = request.POST.get("email", None)
        pwd = request.POST.get("pwd", None)
        print (email, pwd)
        # if email == "wzs@123" and pwd == "wzs":
        request.session["is_login"] = "1"
        user_obj = models.UserInfo.objects.filter(name=email, pwd=pwd).first()

        if user_obj:
            return redirect("/publisher_list/")
        else:
            error_msg = "邮箱/密码错误"
    return render(request, "login.html", {"error":error_msg})


#展示出版社列表
@check_login
def publisher_list(request):
    # 去数据库查出所有的出版社,填充到HTML中,给用户返回
    ret = models.Publisher.objects.all().order_by("id")
    # return render(request, "publisher_list.html", {"publisher_list": ret})
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    #总数据是多少
    total_count = models.Publisher.objects.all().count()
    per_page = 3
    # 总共需要显示多少页码展示
    total_page, m = divmod(total_count, per_page)
    if m:
        total_page +=1
    try:
        page_num = int(page_num)
        # 如果输入的页码数超过了最大的页码数，默认返回最后一页
        if page_num > total_page:
            page_num = total_page
    except Exception as e:
        # 当输入的页码不是正经数字的时候 默认返回第一页的数据
        page_num = 1

    #
    data_start = (page_num-1)*3
    data_end = page_num*3

    #页面上总共展示多少页码
    max_page = 11
    if total_page < max_page:
       max_page =  total_page

    half_max_page = max_page // 2
    #页面上展示的页码到哪儿结束
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page
    #如果当前页减一半 比1还小
    if page_start <= 1:
        page_start = 1
        page_end = max_page
    # 如果 当前页 加 一半 比总页码数还大
    if page_end >= total_page:
        page_end = total_page
        page_start = total_page - max_page + 1

    all_book = models.Publisher.objects.all()[data_start:data_end]

    #自己拼接分页的HTML代码
    html_str_list = []
    #加上第一页
    html_str_list.append('<li><a href="/publisher_list/?page=1">首页</a></li>')
    # 判断一下 如果是第一页，就没有上一页
    if page_num <= 1:
        html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))
    else:
        #加一个上一页的标签
        html_str_list.append('<li><a href="/publisher_list/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))

    for i in range(page_start, page_end+1):
        # 如果是当前页就加一个active样式类
        if i == page_num:
            tmp = '<li class="active"><a href="/publisher_list/?page={0}">{0}</a></li>'.format(i)
        else:
            tmp = '<li><a href="/publisher_list/?page={0}">{0}</a></li>'.format(i)
        html_str_list.append(tmp)

    # 加一个下一页的按钮
    # 判断，如果是最后一页，就没有下一页
    if page_num >= total_page:
        html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        html_str_list.append('<li><a href="/publisher_list/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num + 1))

    # 加最后一页
    html_str_list.append('<li><a href="/publisher_list/?page={}">尾页</a></li>'.format(total_page))
    page_html = "".join(html_str_list)

    return render(request, "publisher_list.html", {"publisher": all_book,"page_html": page_html,"publisher_list": ret})
    

# 添加新的出版社
def add_publisher(request):
    # 如果是POST请求,我就取到用户填写的数据
    error_msg=""
    if request.method == "POST":
        new_name = request.POST.get("publisher_name" , None)
        if new_name:
            # 通过ORM去数据库里新建一条记录
            models.Publisher.objects.create(name=new_name)
            # 引导用户访问出版社列表页,查看是否添加成功  --> 跳转
            return redirect("/publisher_list/")
        else:
            error_msg="出版社名字不能为空"
    # 用户第一次来,我给他返回一个用来填写的HTML页面
    return render(request, "add_publisher.html",{"error":error_msg})


# 删除出版社的函数
# def delete_publisher(request):
#     # 删除指定的数据
#     # 1. 从GET请求的参数里面拿到将要删除的数据的ID值
#     del_id = request.GET.get("id", None)  # 字典取值,取不到返回None值
#     # 如果能取到id值
#     if del_id:
#         # 去数据库删除当前id值的数据
#         # 根据id值查找到数据
#         del_obj = models.Publisher.objects.get(id=del_id)
#         # 删除
#         del_obj.delete()
#         # 返回删除后的页面,跳转到出版社的列表页,查看删除是否成功
#         return redirect("/publisher_list/")
#     else:
#         return HttpResponse("要删除的数据不存在!")

# 删除出版社的函数
def delete_publisher(request):
    # 删除指定的数据
    # 1. 从POST求的参数里面拿到将要删除的数据的ID值
    del_id = request.POST.get("id", None)  # 字典取值,取不到返回None值
    if del_id:
        models.Publisher.objects.filter(id=del_id).delete()
        return HttpResponse("删除成功!")
    else:
        return HttpResponse("要删除的数据不存在!")


#编辑出版社
def edit_publisher(request):
    # 用户修改完出版社的名字,点击提交按钮,给我发来新的出版社名字
    if request.method == "POST":
        # print(request.POST)
        # 取新出版社名字
        edit_id = request.POST.get("id")
        new_name = request.POST.get("publisher_name")
        #更新出版社
        #根据id渠道(取对象)编辑的是哪个出版社
        edit_publisher=models.Publisher.objects.get(id=edit_id)
        #获取对象name值并赋予新的值
        edit_publisher.name=new_name
        edit_publisher.save() #把修改提交到数据库
        # 跳转出版社列表页,查看是否修改成功
        return redirect("/publisher_list/")

    #从GET请求的URL中取到id的参数
    edit_id=request.GET.get("id")
    if edit_id:
        #获取到当前编辑的出版社对象
        publisher_obj=models.Publisher.objects.get(id=edit_id)
        return render(request, "edit_publisher.html", {"publisher":publisher_obj})
    else:
        return HttpResponse("编辑的出版社不存在！")


#展示书籍列表
@check_login
def book_list(request):
    all_book = models.Book.objects.all()
    # return render(request,"book_list.html",{"all_book":all_book})
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Book.objects.all().count()
    per_page = 10
    # 总共需要显示多少页码展示
    total_page, m = divmod(total_count, per_page)
    if m:
        total_page += 1
    try:
        page_num = int(page_num)
        # 如果输入的页码数超过了最大的页码数，默认返回最后一页
        if page_num > total_page:
            page_num = total_page
    except Exception as e:
        # 当输入的页码不是正经数字的时候 默认返回第一页的数据
        page_num = 1

    #
    data_start = (page_num - 1) * 10
    data_end = page_num * 10

    # 页面上总共展示多少页码
    max_page = 11
    if total_page < max_page:
        max_page = total_page

    half_max_page = max_page // 2
    # 页面上展示的页码到哪儿结束
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page
    # 如果当前页减一半 比1还小
    if page_start <= 1:
        page_start = 1
        page_end = max_page
    # 如果 当前页 加 一半 比总页码数还大
    if page_end >= total_page:
        page_end = total_page
        page_start = total_page - max_page + 1

    all_book = models.Book.objects.all()[data_start:data_end]

    # 自己拼接分页的HTML代码
    html_str_list = []
    # 加上第一页
    html_str_list.append('<li><a href="/book_list/?page=1">首页</a></li>')
    # 判断一下 如果是第一页，就没有上一页
    if page_num <= 1:
        html_str_list.append(
            '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num - 1))
    else:
        # 加一个上一页的标签
        html_str_list.append(
            '<li><a href="/book_list/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num - 1))

    for i in range(page_start, page_end + 1):
        # 如果是当前页就加一个active样式类
        if i == page_num:
            tmp = '<li class="active"><a href="/book_list/?page={0}">{0}</a></li>'.format(i)
        else:
            tmp = '<li><a href="/book_list/?page={0}">{0}</a></li>'.format(i)
        html_str_list.append(tmp)

    # 加一个下一页的按钮
    # 判断，如果是最后一页，就没有下一页
    if page_num >= total_page:
        html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        html_str_list.append(
            '<li><a href="/book_list/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num + 1))

    # 加最后一页
    html_str_list.append('<li><a href="/book_list/?page={}">尾页</a></li>'.format(total_page))
    page_html = "".join(html_str_list)
    return render(request, "book_list.html",
                  {"publisher": all_book, "page_html": page_html, "all_book":all_book})

#添加书籍
def add_book(request):
    if request.method == "POST":
        print(request.POST)
        print("="*120)
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title, publisher_id=new_publisher_id)
        return redirect("/book_list/")
    
    #取到所有出版社
    ret = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list":ret})
      
        
#删除书籍
def delete_book(request):
    delete_id = request.POST.get("id")
    models.Book.objects.filter(id=delete_id).delete()
    return HttpResponse("删除成功!")


#编辑书籍
def edit_book(request):
    if request.method == "POST":
        edit_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        # 更新
        edit_book_obj = models.Book.objects.get(id=edit_id)
        edit_book_obj.title = new_title # 更新书名
        edit_book_obj.publisher_id = new_publisher_id # 更新书籍关联的出版社
        #将修改提交到数据库
        edit_book_obj.save()
        return redirect("/book_list/")

    edit_id = request.GET.get("id")
    edit_book_obj = models.Book.objects.get(id=edit_id)
    print(edit_book_obj.id)
    print(edit_book_obj.title)
    print(edit_book_obj.publisher)
    print(edit_book_obj.publisher_id)

    ret = models.Publisher.objects.all()
    return render(
        request,
        "edit_book.html",
        {"publisher_list":ret, "book_obj":edit_book_obj}
    )


#作者列表
@check_login
def author_list(request):
    all_author = models.Author.objects.all()
    # return render(request,"author_list.html",{"author_list": all_author})
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Author.objects.all().count()
    per_page = 10
    # 总共需要显示多少页码展示
    total_page, m = divmod(total_count, per_page)
    if m:
        total_page += 1
    try:
        page_num = int(page_num)
        # 如果输入的页码数超过了最大的页码数，默认返回最后一页
        if page_num > total_page:
            page_num = total_page
    except Exception as e:
        # 当输入的页码不是正经数字的时候 默认返回第一页的数据
        page_num = 1

    #
    data_start = (page_num - 1) * 10
    data_end = page_num * 10

    # 页面上总共展示多少页码
    max_page = 11
    if total_page < max_page:
        max_page = total_page

    half_max_page = max_page // 2
    # 页面上展示的页码到哪儿结束
    page_start = page_num - half_max_page
    page_end = page_num + half_max_page
    # 如果当前页减一半 比1还小
    if page_start <= 1:
        page_start = 1
        page_end = max_page
    # 如果 当前页 加 一半 比总页码数还大
    if page_end >= total_page:
        page_end = total_page
        page_start = total_page - max_page + 1

    all_book = models.Author.objects.all()[data_start:data_end]

    # 自己拼接分页的HTML代码
    html_str_list = []
    # 加上第一页
    html_str_list.append('<li><a href="/author_list/?page=1">首页</a></li>')
    # 判断一下 如果是第一页，就没有上一页
    if page_num <= 1:
        html_str_list.append(
            '<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num - 1))
    else:
        # 加一个上一页的标签
        html_str_list.append(
            '<li><a href="/author_list/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num - 1))

    for i in range(page_start, page_end + 1):
        # 如果是当前页就加一个active样式类
        if i == page_num:
            tmp = '<li class="active"><a href="/author_list/?page={0}">{0}</a></li>'.format(i)
        else:
            tmp = '<li><a href="/author_list/?page={0}">{0}</a></li>'.format(i)
        html_str_list.append(tmp)

    # 加一个下一页的按钮
    # 判断，如果是最后一页，就没有下一页
    if page_num >= total_page:
        html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
    else:
        html_str_list.append(
            '<li><a href="/author_list/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num + 1))

    # 加最后一页
    html_str_list.append('<li><a href="/author_list/?page={}">尾页</a></li>'.format(total_page))
    page_html = "".join(html_str_list)
    return render(request, "author_list.html",
                  {"publisher": all_book, "page_html": page_html,"author_list": all_author})

#添加作者
def add_author(request):
    if request.method == "POST":
        new_author_name = request.POST.get("author_name")
        # post提交的数据是多个值的时候一定会要用getlist,如多选的checkbox和多选的select
        books = request.POST.getlist("books")
        new_author_obj = models.Author.objects.create(name=new_author_name)
        # 把新作者和书籍建立对应关系,自动提交
        new_author_obj.book.set(books)
        return redirect("/author_list/")

    ret = models.Book.objects.all()
    return render(request,"add_author.html",{"book_list": ret})


#删除作者
def delete_author(request):
    delete_id1 = request.POST.get("id")
    models.Author.objects.filter(id=delete_id1).delete()
    return HttpResponse("删除成功!")


#编辑作者
def edit_author(request):
    if request.method == "POST":
        # 拿到提交过来的编辑后的数据
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        # 拿到编辑后作者关联的书籍信息
        new_books = request.POST.getlist("books")
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        edit_author_obj.name = new_author_name
        edit_author_obj.book.set(new_books)
        edit_author_obj.save()
        return redirect("/author_list/")

    edit_id = request.GET.get("id")
    edit_author_obj = models.Author.objects.get(id=edit_id)

    ret = models.Book.objects.all()
    return render(request, "edit_author.html", {"book_list": ret, "author": edit_author_obj})

def test(request):
    print(request.GET)
    print(request.GET.get("id"))
    return HttpResponse("ok")




'''
print(request.GET)获得

http://127.0.0.1:8000/test/
返回：<QueryDict: {}>

http://127.0.0.1:8000/test/?name=wu
返回：<QueryDict: {'name': ['wu']}>

http://127.0.0.1:8000/test/?name=wu&pwd=123
返回：<QueryDict: {'name': ['wu'], 'pwd': ['123']}>


print(request.GET)
print(request.GET.get("id"))

网页：http://127.0.0.1:8000/test/?id=1
返回：
<QueryDict: {'id': ['1']}>
1
'''

