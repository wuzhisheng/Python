''''''
'''
#闭包函数 -  内部的函数 引用了 外部函数的变量
#inner就是一个闭包函数 因为inner引用了一个外部outer的a,b
判断闭包函数： __closure__   不是闭包函数会返回None值
 '''
def outer():
    a = 1
    b = 'str'
    def inner():
        print(a,b)
    print(inner.__closure__)   # inner就是一个闭包函数 因为inner引用了一个外部outer的a,b
outer()
print(outer.__closure__)


#输出的__closure__为None ：不是闭包函数
name = 'egon'
def func2():
    def inner():
        print(name)
    print(inner.__closure__)
    return inner
f2 = func2()
f2()


'''
# 闭包函数：内部函数使用了外部函数的变量
(其创建一个空间会重复使用，直至不用。其到缓存作用)
# 1.不需要重复的去调用外部函数 节省了重复开辟空间存储a,b的时间
# 2.保护了a,b只能在局部被使用

内部函数包含对外部作用域而非全剧作用域名字的引用
'''
#函数调用多少次，这会创建多少次空间，调用完则会被销毁
def outer():
    a = 1
    b = 'str'
    print(a,b)
outer()
outer()

#闭包函数
def outer():
    a = 1
    b = 'str'
    def inner():
        print(a,b)
    return inner

'''
# 为什么要用闭包函数来实现下面的功能
# 把读文件的逻辑放在全局
# with open('file') as f:
#     content = f.read()
# 一旦content被别人修改了，那么原来的content就再也找不回来了

# 把逻辑放在函数中
# def read():
#     with open('file') as f:
#         content = f.read()
#         return content
# 每次调用read都需要读同一个文件，打开读关闭操作重复执行浪费时间，
'''

# 闭包函数
def read(): #1
    with open('file') as f: #3
        content = f.read() #4
    def inner(): #5
        return content #8
    return inner #6
inn = read() #2 #inn的内存地址就是inner函数的内存地址
content1 = inn() #7 #inn()相当于inner()将内存地址具象化
print(content1) #9


from urllib.request import urlopen
def func(url):
    ret = urlopen(url)
    content = ret.read().decode('utf-8')
    def inner():
        return content
    return inner
inn = func('https://www.cnblogs.com/Eva-J/articles/9600484.html')
inn()

# 做缓存

# def fun1():
#     x=2
#     def fun2():
#         x *= x
#         return x
#     return fun2
#内部函数定义x时，python认为x是局部变量是，外部函数的x被屏蔽起来，所以找不到值

def fun1():
    x=2
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2

fun1()()


def funx(x):
    def funy(y):
        return x*y
    return funy
i=funx(8)
print(i(5))
#或者
print(funx(8)(5))