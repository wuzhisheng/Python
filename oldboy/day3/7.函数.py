''''''
'''
函数的定义和调用
定义：def 关键词开头，空格之后接函数名称和圆括号()，最后还有一个":"
调用：函数名()

作用
# 提高代码的复用性
# 代码的可读性
'''
#1. 函数定义和调用/ 形参和实参
s2 = 'hello world'
def len():  # 定义  形式参数
    count = 0
    for i in s2:
        count+=1
    print(count)
len() # 调用  实际参数


# 2.return返回值和返回值的接受
s = 'hello,world'
s1 = 'hi,chileme'
print(len(s)>len(s1))

def my_len(参数):     # 定义 形式参数
    count = 0
    for i in 参数:
        count += 1
    return count
ret = my_len(s1)
print(ret)
print(my_len(s)>my_len(s1))

# 只要是函数 就有返回值
# 如果需要返回某个值 ：return关键字
    # return的作用:
        # 1.将函数中的某个变量返回
            # 不写/只写return ： 没有特意的返回某个值,默认返回None
            # return n        :有一个返回值
            # return n1,n2,n3 :返回多个值
                # 如果只有一个变量接收：收到一个元组
                # 如果用多个变量接收：返回几个值就用几个变量来接受
        # 2.结束一个函数的运行

# return n1,n2,n3 :返回多个值
                # 如果只有一个变量接收：收到一个元组


#只要是函数 就有返回值
#没有return 返回None
def mylen():
    s1 = "hello world"
    length = 0
    for i in s1:
        length = length+1
    print(length)
str_len = mylen()
print(str_len)

#不写/只写return ： 没有特意的返回某个值,默认返回None
#且return会结束整个函数
def my_iter():
    for i in range(1,100):
        print(i)
        if i % 5 == 0:
            return #
ret = my_iter()
print('-->',ret)


def ret_demo2():
    return 1,['a','b'],3,4
#返回多个值，用一个变量接收
ret2 = ret_demo2()
print(ret2)
#返回多个值，用多个变量接收
a,b,c,d = ret_demo2()
print(a,b,c,d)

'''
>>> 1,2 #python中把用逗号分割的多个值就认为是一个元组。
(1, 2)
>>> a,b,c=(1,2,3)
>>> a
1
>>> c
3
#
也适用于字符串、列表、字典、集合
>>> a,b = {'name':'eva','age':18}
>>> a
'name'
>>> b
'age'
'''

# 3. 参数
# 可以传多个参数么？可以传任意多个，但是建议你只传5个以下
#传参：mylen函数要计算的字符串是谁，这个过程就叫做传递参数
#s1（形参）和hello world （实参）
def mylen(s1):
    length = 0
    for i in s1:
        length = length+1
    return length
str_len = mylen("hello world")
print(str_len)


def mul_str(s,n):
    return s*n
for i in range(1,20):
    res = mul_str('*',i)
    print(res)

#1.位置参数
def mymax(x,y):
    the_max = x if x > y else y
    return (the_max)
ma = mymax(10,20)

    #关键字传值
def mymax(x,y):
    print(x,y)
    the_max = x if x > y else y
    return the_max
ma = mymax(20,y=10)
print(ma)

#2.默认参数
def stu_info(name,sex = "male"):
    print(name,sex)
stu_info('alex')
stu_info('eva','female')

    #3.参数陷阱：默认参数是一个可变数据类型
def defult_param(a,l = []):
    l.append(a)
    print(l)
defult_param('alex')
defult_param('egon')


# 动态参数 : args  参数  以 元组 形式
def mul(*l):  # l = (5,4,3,2,1)
    count = 1
    for i in l:
        count *= i
    return count
print(mul())
print(mul(5,4,3,2,1))
l = [5,4,3,2,1]
print(mul(*l))

#动态参数 : **kwargs   参数  以 字典 形式
def func(**k):
    print(k)

func(mode='r',encoding='utf-8',age = 18)
func(1,2,3,4)   # 报错

stu1 = {'name':'李青','age':20}
func(**stu1) # func(name = '李青', age=20)



# 站在实参的角度上来看，传递参数的时候有哪些方法
def copy_file(filename,new_name):
    with open(filename,encoding='utf-8') as f1,\
        open(new_name,mode='w',encoding='utf-8') as f2:
        content = f1.read()
        f2.write(content)
copy_file('a.txt','a_copy.txt')    # 按照位置传参数
copy_file(new_name = 'a_copy2.txt',filename = 'a.txt')# 按照关键字传参数,可以不按照顺序传
copy_file('a.txt',new_name = 'a_copy3.txt')# 按照位置和关键字传参数，先按照位置传，再按照关键字传



# 几种参数之间有没有什么特殊的先后顺序
    # 定义参数 ： 位置参数  *args 默认参数 **kwargs
    # 调用函数 ： 按照位置传 ，按照关键字传
def func(a,b,*args,default= 'male',**kwargs):
    print(a,b)
    print(*args)
    print(default)
    print(kwargs)

func(1,2,3)
func(1,2,3,name='alex',age=83)
l = [1,2,3,4]
dic = {'name':'alex','age':83,'default':'female'}
func(*l,*dic)  # func(1,2,3,4,'name','age')
func(*l,**dic)  # func(1,2,3,4,name='alex',age=83)

def func(a,b,*args,default= 'male',**kwargs):
    print(a,b)
    print(*args)
    print(default)
    print(kwargs)
func(1,2)
func(1,2,3,name = 3,age = 4)
# 想用这个default

# 站在定义函数和调用函数的角度上分别来看 形参和实参
# 函数定义 - 形参
    # 位置参数
    # *args
    # 默认参数
    # **kwargs

# 函数的调用阶段
    # 按照位置传参 ： 值1，值2 值3....  / *[值1，值2 值3]
    # 按照关键字传参 ： name1=值1,name2=值2../**{'name1':值1,'name2':值2}




