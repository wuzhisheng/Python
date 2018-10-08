''''''
'''
迭代:将某个数据集内的数据“一个挨着一个的取出来”
字符串、列表、元组、字典、集合都可以被for循环,可迭代的
Iterable:可迭代的

迭代：满足迭代协议
迭代器遵循迭代器协议：必须拥有__iter__方法和__next__方法
遍历之前,先调用对象的__iter__方法将其转换成一个迭代器，然后使用迭代器协议去实现循环访问

被for循环的都是可迭代的，要想可迭代，内部必须有一个__iter__
'''

'''
迭代类似循环
每次重复的过程被称为一次迭代的过程
每次迭代的结果被用作下次迭代的初始值
提供迭代方法的容器称为迭代器（字符串、列表、元组、字典、集合）
'''
for i in "wzs":
    print(i)
#字符串'wzs'为容器及迭代器
#for 触发这个迭代器的迭代功能
#迭代操作：每次从容器中一次拿出一个数据

'''
对容器对象调用iter()则得到迭代器
调用next()迭代器会返回下一个值
若迭代器没有值可返回则显示：StopIteration
'''
#for 的工作过程
string="wzs"
it=iter(string)
while True:
    try:
        each=next(it)
    except StopIteration:
        break
    print (each)





'''
迭代器有的好处是可以节省内存。

我们也需要节省内存,就只能自己写。
生成器:自己写的这个能实现迭代器功能的东西
(生成器是迭代器的一种实现)

一个包含yield关键字的函数就是一个生成器函数

yield从函数中返回值
调用生成器函数不会得到返回的具体的值，而是得到一个可迭代的对象
每一次获取这个可迭代对象的值，就能推动函数的执行，获取新的返回值。直到函数执行结束

普通函数：
从头开始执行，至return，所有语句执行完，则完毕。所有工作及
保存在局部变量中的数据都丢失。再次调用重头开始

生成器：
实现协同程序：生成器可以暂时挂起函数，并保留函数的局部变量等数据
等再次调用时，从上次暂停的位位置继续执行下去。
'''
def gen():
    print("执行生成器")
    yield 1
    yield 3
G = gen()
print(next(G))
print(next(G))
#若再调用一个next(G)则会返回 StopIteration
#for 自动调用next()和处理StopIteration
for i in gen():
    print(i)




def produce():
    for i in range(2000000):
        yield "生产了第%s件衣服"%i
product_g = produce()
print(product_g.__next__()) #要一件衣服
print(product_g.__next__()) #再要一件衣服
print(product_g.__next__()) #再要一件衣服

num = 0
for i in product_g: #要一批衣服，比如5件
    print(i)
    num +=1
    if num == 5:
        break