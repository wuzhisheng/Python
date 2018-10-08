''''''
'''
内置函数
'''
#内存相关：
#id(o) o是参数，返回一个变量的内存地址
#hash(o) o是参数，返回一个可hash变量的哈希值，不可hash的变量被hash之后会报错。
t = (1,2,3)
l = [1,2,3]
print(hash(t)) #可hash
print(hash(l)) #会报错

#dir() 默认查看全局空间内的属性
print(dir(list)) #查看列表的内置方法

#zip()
a=[1,2,3]
b=[4,5,6]
c=[4,5,6,7,8]
zipped=zip(a,b) #打包为元组的列表
#[(1,4),(2,5),(3,6)]
zip(a,c) #元素个数与最短的列表一致
#[(1,4),(2,5),(3,6)]
zip(*zipped)#与zip相反，*zipped可理解为解压


#map()
def square(x):
    return x ** 2
map(square,[1,2,3,4,5]) # 计算列表各个元素的平方

map(lambda x:x**2,[1,2,3,4,5]) #使用lamba匿名函数

map(lambda x,y:x+y,[1,2,3,4,5],[1,2,3,4,5])

#filter() 过滤器
temp=filter(None,[1,0,False,True])  #过滤None值
print(list(temp))

def odd(x):
    return x % 2
temp=filter(odd,range(10)) #过滤偶数值
print(list(temp))

list(filter(lambda x:x % 2,range(10)))
'''
匿名函数
函数名 = lambda 参数 ：返回值
参数可以有多个，用逗号隔开
匿名函数不管逻辑多复杂，只能写一行，且逻辑执行结束后的内容就是返回值
返回值和正常的函数一样可以是任意数据类型
'''
res = map(lambda x:x**2,[1,5,7,4,8])
for i in res:
    print(i)

'''
两个元组(('a'),('b')),(('c'),('d'))，请使用python中匿名函数
生成列表[{'a':'c'},{'b':'d'}]
'''
#1
test = lambda t1,t2 :[{i:j} for i,j in zip(t1,t2)]
print(test((('a'),('b')),(('c'),('d'))))
#2
print(list(map(lambda t:{t[0]:t[1]},zip((('a'),('b')),(('c'),('d'))))))
#3
print([{i:j} for i,j in zip((('a'),('b')),(('c'),('d')))])













