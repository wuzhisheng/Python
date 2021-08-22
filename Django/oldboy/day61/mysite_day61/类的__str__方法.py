#一
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("小黑", 18)
print(p)
#打印个对象和内存地址
#<__main__.Person object at 0x0000000001F29390>

#2
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "<{} {}>".format(self.name, self.age)
    
p = Person("小黑", 18)
#print的时候，直接调用__str__方法
print(p)
p2 = Person("高材生", 9000)
print(p2)
