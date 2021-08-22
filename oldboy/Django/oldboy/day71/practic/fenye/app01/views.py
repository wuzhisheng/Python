from django.shortcuts import render

# Create your views here.

from app01 import models

def books(request):

    # all_book = models.Book.objects.all()[:10]
    # return  render(request,"books.html",{"books":all_book})
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    page_num = int(page_num)
    #
    data_start = (page_num-1)*10
    data_end = page_num*10

    #每一页显示多少条数据
    per_page = 10

    #总共需要显示多少页
    total_count = models.Book.objects.all().count()
    total_page, m = divmod(total_count, per_page)
    if m:
        total_page +=1

    all_book = models.Book.objects.all()[data_start:data_end]

    #自己拼接分页的HTML代码
    html_str_list = []
    for i in range(1, total_page+1):
        tmp = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)
        html_str_list.append(tmp)
    page_html = "".join(html_str_list)

    return render(request, "books.html", {"books": all_book,"page_html": page_html})