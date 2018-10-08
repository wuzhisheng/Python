''''''

#程序执行流程序号
aaa = 0  #1
def outer():  #2
    aaa = 1  #4
    print('in outer',aaa)  #5
    def inner():  #6
        aaa = 2  #8
        print('in inner',aaa)  #9
    inner()  #7
outer()  #3
print('global : ',aaa)  #10

'''
命名空间：
解释器将函数变量名和值关系存入读入内存
再执行时，解释器会开辟一块内存空间来存储这个函数里的内容
数中的变量只能在函数的内部使用，并且会随着函数执行完毕，这块内存中的所有内容也会被清空

全局命名空间：创建的存储变量名与值的关系
局部命名空间：函数的运行中开辟的临时的空间
内置命名空间：中存放了python解释器为我们提供的名字：input,print,str,list,tuple..

加载顺序：内置命名空间(程序运行前加载)->全局命名空间(程序运行中：从上到下加载)->局部命名空间(程序运行中：
调用时才加载)

在局部调用：局部命名空间->全局命名空间->内置命名空间
在全局调用：全局命名空间->内置命名空间

函数外部定义的所有变量 都是全局变量
    函数内部定义的所有变量 都是局部变量
在函数的内部可以引用函数外部的变量，但不能修改这个变量
如果需要在局部修改全局的变量 需要在局部声明global n
在全局不可以使用局部的变量
'''
def func():
    a = 12
    b = 20
    print(locals())
    print(globals())
func()

#全局不可以使用局部的变量
def qqxing():
    a = 1
print(a)

#函数的内部修外部变量，要使用global
n = 0
def func():
    global n
    n += 1
func()
print(n)


'''
#global使用
'''
a= 0
def outer():
    global a#内部可修改全局变量
    a += 1
    print('in outer',a)
    def inner():
        print('in inner',a)
    inner()
outer()
print('global : ',a)


'''
nonlocal 
用来找内层函数中修改上一层函数中的变量（只对上一层生效），但是不能用来修改全局变量
'''
aaa = 0
def outer():
    aaa = 1
    def inner():
        nonlocal aaa
        aaa += 2
        print('in inner',aaa)   # 3
    inner()
    print('in outer', aaa)   # 3
outer()
print('global : ',aaa)  # 0

# nonlocal : 用来找内层函数中修改上一层函数中的变量，但是不能用来修改全局变量
#若上层没有则找上上一层
def outer():
    a = 1
    def func():
        a = 2
        def inner():
            nonlocal a
            a += 2
            print('inner a ',a) #4
        inner()
        print('in func',a) #4
    func()
    print('in outer ',a) #1
outer()
'''
之后你写程序 要尽量避免使用 global和nonlocal关键字
因为在函数的内部去修改全局变量 是容易导致数据错乱的

如果需要在函数中用到全局变量 应该采用传递参数的形式来进行使用
如果在函数内涉及到变量的修改的话 那么记得修改之后的结果要返回
'''

'''
作用域
全局作用域：任意位置都能被引用、全局有效
局部作用域：局部名称空间，只能在局部范围内生效
'''



'''
函数的嵌套定义
每一个函数在执行的时候都会创建一个局部命名空间/临时命名空间
在执行完这个函数之后，这个临时的空间还会被销毁
当内部的函数在进行变量的引用的时候，如果内部的命名空间有这个值，就引用这个值
如果内部没有，可以引用外部函数的变量，如果外部函数也没有，可以引用全局的变量
'''
n  = 100
# 函数的嵌套调用
def wahaha():
    print('in wahaha')

def func():
    print('in func')
    wahaha()
func()


def f1():
    print("in f1")
    def f2():
        print("in f2")
    f2()
f1()


def max2(x,y):
    m = x if x>y else y
    return m
def max4(a,b,c,d):
    res1 = max2(a,b)
    res2 = max2(res1,c)
    res3 = max2(res2,d)
    return res3
print(max4(23,-7,31,11))


'''
值语义 C
引用语义 python
    使用的变量 都是内存地址

列表作为一个位置参数 ：在函数中修改这个位置参数，函数外也会变
不可变数据类型作为一个位置参数 ：在函数中修改这个位置参数，函数外不会变
列表作为一个默认参数 ：多次调用这个函数，共享这个列表
'''
# 一阶函数
# 可变数据类型作为参数，如果在函数的内部发生了变化，在函数的外部也同样生效
l = []
def func(l):
    l.append(1)
    print('in func',l)

func(l)
print(l)

# 对于不可变数据类型，作为参数传递到函数中的修改 不会影响到函数外部的变量
a = 10
def func(a):
    a = 20
    print('in func', a)
func(a)
print(a)

# 默认参数的陷阱,如果默认参数是一个可变数据类型
# 那么多次调用同一个函数，是共用这个参数的
lst = []
def func(l = lst):
    l.append(1)
    print(l)

func()
func()
func()
func([]) #将会用一个新的列表



'''
函数名本质上就是一个变量，保存了函数所在的内存地址

函数可以赋值给一个变量
    可以作为参数
    可以作为返回值
    可以作为容器类型的一项

函数的名字只是一个普通的变量
任何一个内容是函数地址的变量 加上括号都相当于调用这个函数

第一类对象
    函数
    所有数据类型都是
'''
def qq(arg):
    print(arg)

def ww():
    def inner():
        print('inner')
    return inner

def func():
    print('in func')

print(func) #函数名本质上就是函数的内存地址

wrap = func
print(wrap) #打印内存地址
wrap() #打印值

#函数可以被引用
qq(func) #函数名本质上就是函数的内存地址
qq(func()) #in func +（） 打印值
print(ww()) #打印内存地址

#可以被当作容器类型的元素
l = [ww,func,qq]
print(l)








