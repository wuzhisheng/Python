#更详细解析网址
#http://python.jobbole.com/85056/

## 计算一个程序的执行效率  0.3s之内的响应时间
import time  # 时间控制的代码
def func1():
    start = time.time()
    time.sleep(0.1)
    print('in func1')
    print(time.time() - start)
func1()


#还是改变了这个函数的调用方式:cal_time(my_func)
import time
def my_func():
    time.sleep(0.1)
    print('欢迎进入XXX游戏')
def my_func2():
    time.sleep(0.1)
    print('欢迎进入XXX游戏')
def cal_time(func):   # func == my_func
    start = time.time()
    func()
    print(time.time() - start)
cal_time(my_func)
cal_time(my_func2)


'''
问题

import time
def timer(func):
    start = time.time()
    func()
    print(time.time() - start)
def func1():
    print('in func1')
func1 =timer #要是能这样的就完美了。。。可惜报错
func1()

timer方法需要传递一个func参数，我们不能在赋值的时候传参，因为只要执
行func1 = timer(func1)，timer方法就直接执行了，下面的那句func1根本就没有意义
'''

#闭包
def func():
    def func1():
        print('i\'m func1')
    return func1

f = func()
f()
print('函数func1的内存地址为：',f)
'''
函数func()内部定义了另外一个函数func1()，最终return的是func1的内存地址。
函数定义完后，在全局把func()赋值给变量f，此时f中拿到的是func1的内存地址，这时候你可以把f看成是
func1，进行f()操作相当于调用func1()

f相当于func1，那么为何不在全局中直接调用func1()呢？答案是不行~因为
func1()是在全局的函数func()里面定义的，全局情况下只能调用func()，不可以直接调用func()里面的函数

我们要想在全局情况下调用“全局函数”内部定义的函数，就必须令该全局函数返回“内部函数”的内存
地址，然后将该内存地址赋值给一个变量，通过调用这个变量来实现“全局调用内部函数”，而此时，这个“内部
的函数”就称为“闭包”。
'''



import time
def func1():
    print('in func1')

def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
# print(func1)  #显示func1内存地址
# print(timer) #显示timer内存地址
# print(timer(func1)) #显示inner内存地址
func1 = timer(func1) #显示inner内存地址
func1() #将inner内存地址具象化

'''
装饰器的本质：一个闭包函数
装饰器的功能：在不修改原函数及其调用方式的情况下对原函数功能进行扩展

装饰器作用：装饰原有的函数
函数func(a, b)，它的功能是求a,b的差值，我现在有一个需求，就是想对函数功能再装饰下，
求完差值后再取绝对值，但是不能在func函数内部实现，这时候就需要装饰器函数了，
比如func = decorate(func)函数，将func函数作为参数传递给decorate函数，由decorate来丰富func函数，
丰富完成后再返回给func,此时func的功能就丰富了
'''

#一：不带参数的装饰器
#@timer #==> func1 = timer(func1) = inner
import time
def timer(func):
    def inner():
        start = time.time()
        func()
        print(time.time() - start)
    return inner
@timer #==> func1 = timer(func1)
def func1():
    print('in func1')
func1()
'''
这里我们先定义了一个装饰器timer()，而timer函数里面的inner函数就是一个闭包。当我们在函数
func1定义前加上@timer时，这个语句相当于：func1 = timer(func1)。也就是说，我们在进行不带参数的装
饰器的调用时，相当于把下面的函数名当做参数传给了@后面的函数，@timer也就相当于执行了timer(func1)。
后面就好理解了：timer()函数返回了inner函数的内存地址，下面的func1()其实就调用了“闭包”inner()，进行
了inner()函数里面的操作
'''



'''以上装饰器都是装饰不带参数的函数，现在要装饰一个带参数的函数怎么办呢？'''
# 新需求
# 在调用my_func2的时候 能直接计算出myfunc2的执行时间就好了
# 让你调用myfunc2，能够保留myfunc2的所有功能和他的调用方式的同时，还能够统计自己执行的时间
import time
def timer(func):
    def inner(*args,**kwargs):
        start = time.time()
        re = func(*args,**kwargs)
        print(time.time() - start)
        return re
    return inner

@timer #==> func1 = timer(func1) = inner
def func1(a,b):
    print('in func1')

@timer #==> func2 = timer(func2) = inner
def func2(a):
    print('in func2 and get a:%s'%(a))
    return 'fun2 over'

func1('aaaaaa','bbbbbb')
print(func2('aaaaaa'))


# 装饰器 ：在不改变一个函数的调用方式，和函数内部的代码的同时，在这个函数的前、后添加功能

# l = ('王者','荣耀')
# def func(a,b):
#     print(a,b)
#
# func(l[0],l[1])
# func(*l)

'''
# 装饰器的固定模板
'''
#1
def wrapper(func):
    def inner(*args,**kwargs):
        print('''在执行被装饰函数之前要做的事儿''')
        ret = func(*args,**kwargs)   # 执行被装饰的函数 得到返回值ret
        print('''在执行被装饰函数之后要做的事儿''')
        return ret                   # 将被装饰函数的返回值返回
    return inner

#2
@wrapper
def wahaha(a,b,c):
    print('我是被装饰的函数',a,b,c)
wahaha(1,2,3)

#====================
def index():
    '''这是一个主页信息'''
    print('from index')
print(index.__doc__) #查看函数注释的方法
print(index.__name__) #查看函数名的方法

from functools import wraps
def deco(func):
    @wraps(func) #加在最内层函数正上方
    def wrapper(*args,**kwargs):
      return func(*args,**kwargs)
    return wrapper
@deco
def index():
    '''哈哈哈哈'''
    print('from index')
print(index.__doc__)
print(index.__name__)

'''
装饰器的主要功能：
在不改变函数调用方式的基础上在函数的前、后添加功能。

遵守开放封闭原则
1.允许代码扩展、添加新功能
2.修改封闭：修改，可能影响其他已经在使用该函数的用户
'''



# 登陆验证
# logined = False
# def login(func):
#     def inner(*args,**kwargs):
#         '''登陆逻辑'''
#         global logined
#         if not logined:
#             username = input('username : ')
#             password = input('password : ')
#             if username == 'alex' and password == 'alex3714':
#                 logined = True
#         if logined:
#             ret = func(*args, **kwargs)   # 被装饰的函数
#             return ret
#     return inner
#
# @login
# def select():
#     print('查询数据')
#
# @login
# def delete():
#     print('要删除数据')
#
# @login
# def set():
#     print('要修改数据')
#
# set()
# select()
# delete()


# 如果我调用set的时候没有登陆，那么应该先登录
# select delete set都不需要再登陆


# 日志记录
# def log(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         print('%s %s被执行了'%(time.strftime('%Y-%m-%d %H:%M:%S'),func.__name__))
#         return ret
#     return inner
#
# @log
# def select():
#     print('查询数据')
# #
# @log
# def delete():
#     print('要删除数据')
# #
# @log
# def set():
#     print('要修改数据')
#
# select()
# delete()
# print(set.__name__)
# print(delete.__name__)
#
# func = set
# print(func.__name__)

# 给add添加一个装饰器，如果这个add两个数a,b是结算过的值，那么不要用add再计算一次，而是直接把之前计算的结果返回
# def wrapper(func):
#     dic = {}
#     def inner(*args,**kwargs):
#         args_t = args if args else tuple((kwargs['a'],kwargs['b']))
#         if args_t in dic:
#             return dic[args_t]
#         else:
#             ret = func(*args,**kwargs)   # add
#             dic[args_t] = ret
#         return ret
#     return inner
#
# @wrapper
# def add(a,b):
#     print('执行我啦')
#     return a+b
# #
# print(add(a = 1,b = 2))
# print(add(b = 2,a = 1))
# print(add(1,2))
# print(add(3,4))
# print(add(3,4))
# print(add(3,4))
# print(add(3,4))
# print(add(1,2))

# 三元运算符
# a = 10
# b = 11
# max = 0
# if a > b:
#     max = a
# else:
#     max = b
#
# max = True if a>b else False
# max = a if a>b else b

# args = ()
# kwargs = {'a':1,'b':2}
#(1,2) {}
# if args:
#     args_lst = args
# else:
#     args_lst = tuple(kwargs.values())
# print(args_lst)

# args_lst =args  if args else tuple(kwargs.values())

# def my_pop(l,index = None):
#     index = index if index else 0
#     print(l.pop(index))
# l = [1,2,3]
# my_pop(l)


# 三元运算符
# 变量 = 条件成立的时候返回的值 if 条件 else 条件不成立的时候返回的值

# 装饰器的应用
# 计算时间差
# 登陆验证 ： 一次登陆 处处可以执行
# 日志记录
# 给add函数装饰功能

# time模块的使用
# import time
# time.time() 当前时间 以秒为单位的浮点数
# time.strftime('%Y-%m-%d %H:%M:%S') 当前时间 字符串格式的
# time.sleep(0.1)  表示程序在这里停止0.1



