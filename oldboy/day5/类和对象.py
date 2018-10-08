''''''

'''
面向过程 VS 面向对象
面向过程的程序设计的核心是过程（流水线式思维），过程即解决问题的步骤，面向过程的设计就好比精心设计好一条
流水线，考虑周全什么时候处理什么东西。
优点是：极大的降低了写程序的复杂度，只需要顺着要执行的步骤，堆叠代码即可。
缺点是：一套流水线或者流程就是用来解决一个问题，代码牵一发而动全身。
应用场景：一旦完成基本很少改变的场景，著名的例子有Linux內核，git，以及Apache HTTP Server等


面向对象的程序设计的核心是对象
优点是：解决了程序的扩展性。对某一个对象单独修改，会立刻反映到整个体系中，如对游戏中一个人物参数的特征和
技能修改都很容易。
缺点：可控性差，无法向面向过程的程序设计流水线式的可以很精准的预测问题的处理流程与结果，面向对象的程序一
旦开始就由对象之间的交互解决问题，即便是上帝也无法预测最终结果。于是我们经常看到一个游戏人某一参数的修改
极有可能导致阴霸的技能出现，一刀砍死3个人，这个游戏就失去平衡。
应用场景：需求经常变化的软件，一般需求的变化都集中在用户层，互联网应用，企业内部软件，游戏等都是面向对象
的程序设计大显身手的好地方。

面向对象编程可以使程序的维护和扩展变得更简单，并且可以大大提高程序开发效率 ，另外，基于面向对象的程序可以
使它人更加容易理解你的代码逻辑，从而使团队开发变得更从容。
'''

'''
对象=属性＋方法
对象的特征：属性（变量）
对象的行为：方法（函数）
'''

class Turtle:#类名以大写字母开头
    color='green' #属性（变量）
    weight=10
    def climb(self): #方法（函数）
        print('我正往前爬')
    def run(self):
        print('我往前飞')
'''
定义对象的特征（属性）+行为（方法）还不是完整的对象。定义这些称为 类
用 类 的一个实例称为 对象（叫实例对象）

类相当于玩具模具，依照模具 做出来的玩具 叫对象 

赋值不是必须的，但如果没有把创建好的实例对象赋值给一个变量,则这个对象没法使用

在python中，用变量表示特征，用函数表示技能，因而具有相同特征和技能的一类事物就是‘类’，对象是则是这一类
事物中具体的一个。
'''
tt=Turtle() #类的实例化 即对象
tt.climb() # 调用对象里的方法
tt.run()

'''
类属性的补充

一：我们定义的类的属性到底存到哪里了？有两种方式查看
dir(类名)：查出的是一个名字列表
类名.__dict__:查出的是一个字典，key为属性名，value为属性值
二：特殊的类属性
类名.__name__# 类的名字(字符串)
类名.__doc__# 类的文档字符串
类名.__base__# 类的第一个父类(在讲继承时会讲)
类名.__bases__# 类所有父类构成的元组(在讲继承时会讲)
类名.__dict__# 类的字典属性
类名.__module__# 类定义所在的模块
类名.__class__# 实例对应的类(仅新式类中)
'''


'''
面向对象编程
#self
类比作图纸，那么由类实例化的对象为房子。可以根据该图纸设计N个相同房子
而self相当于每个房子的门牌号

由同一个类生成无数对象，当一个对象的方法被调用时，对象会将自身的引用作为第一个参数传给该方法

class 类名:
    def __init__(self,参数1,参数2):
        self.对象的属性1 = 参数1
        self.对象的属性2 = 参数2
    def 方法名(self):pass
    def 方法名2(self):pass
对象名 = 类名(1,2) #对象就是实例，代表一个具体的东西
#类名() : 类名+括号就是实例化一个类，相当于调用了__init__方法
#括号里传参数，参数不需要传self，其他与init中的形参一一对应
#结果返回一个对象
对象名.对象的属性1 #查看对象的属性，直接用 对象名.属性名 即可
对象名.方法名() #调用类中的方法，直接用 对象名.方法名() 即可
'''
class Ball:
    def setName(self,name):
        self.name=name
    def kick(self):
        print("我叫%s" % self.name)
a=Ball()
a.setName("路飞")
a.kick()

b=Ball()
b.setName('索隆')
b.kick()

'''
__init__()
'''
# 只要实例化一个对象，这个方法会在对象被创建时自动调用
class Potato:
    def __init__(self,name):
        self.name=name
    def kick(self):
        print("我是%s" % self.name)

p=Potato("土豆")
p.kick()


class Person: # 定义一个人类
    role = 'person' # 人的角色属性都是人
def __init__(self, name, aggressivity, life_value):
    self.name = name # 每一个角色都有自己的昵称;
    self.aggressivity = aggressivity # 每一个角色都有自己的攻击力;
    self.life_value = life_value # 每一个角色都有自己的生命值;
def attack(self,dog):
    # 人可以攻击狗，这里的狗也是一个对象。
    # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
    dog.life_value -= self.aggressivity

# 对象是关于类而实际存在的一个例子，即实例
# 对象/实例只有一种作用：属性引用
egg = Person('egon',10,1000)
print(egg.name)
print(egg.aggressivity)
print(egg.life_value)
print(egg.attack)




'''
公有和私有
'''
#python默认上对象的属性和方法都是公开的,直接 . 便可直接访问
class Person:
    name="wzs"
p=Person
print(p.name)

#在python定义私有变量需在变量名或函数名前上加 __(双下划线)
class Person:
    __name="wzs"
p=Person
#print(p.__name) #发现该出错

print(p._Person__name) #可以
#说明python只是用__将变量进行改名。
#python的类没有控制权限，所有变量名可以被外部调用
#其是 伪私有



'''
继承

class ParentClass1: #定义父类
    pass
class ParentClass2: #定义父类
    pass
class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
    pass
class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
    pass
'''
#被继承的类：基类，父类，超类
#继承者：子类（可继承它的父类的任何属性和方法）
class Parent:
    def hello(self):
        print("正在调用父类的方法")
class Child(Parent):
    pass
p=Parent()
p.hello()

c=Child()
c.hello()

#===================================
import random as r
class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        self.x-=1
        print("我的位置是:",self.x,self.y)

class Carp(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        self.hungry=True
    def eat(self): #派生：鲨鱼除继承fish外还有吃技能
        if self.hungry:
            print("有东西吃")
            self.hungry=False
        else:
            print("太撑了，吃不下")

fish=Fish()
fish.move()
carpfish=Carp()
carpfish.move()
shark=Shark()
shark.eat()
shark.eat()
#shark.move()
#发现shark继承不了Fish中属性
#因在Shark类中，重写了__init__,但新的__init__中没有初始化鲨鱼的x坐标和y坐标
#所以要想调用Fish中move方法，需在重写__init__时，先调用基类Fish的__init__方法
'''
1.调用未绑定的父类方法
'''
class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        self.hungry=True

shark=Shark()
shark.move()
'''
使用super函数
不需要给出任何基类的名字
'''
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
shark=Shark()
shark.move()

'''
多重继承
尽量少用，其容易导致代码混乱
'''
class Base1:
    def foo1(self):
        print("我是Base1")

class Base2:
    def foo2(self):
        print("我是Base2")

class C(Base1,Base2):
    pass
c=C()
c.fool()
c.foo2()
#可用组合解决
'''
组合
直接把需要的类放进实例化
'''
class Turtle:
    def __init__(self,x):
        self.num=x

class Fish:
    def __init__(self,x):
        self.num=x

class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def print_num(self):
        print("有%s只乌龟,小鱼有%d条" % (self.turtle.num,self.fish.num))

pool=Pool(1,10)
pool.print_num()



'''
类，类的对象，实例对象
'''
class C: #类
    count=0

a=C() #类的对象
b=C()
print(a.count,b.count)
b.count+=10  #实例对象b的count属性进行赋值后，就覆盖类对象的C的count属性
print(a.count,b.count)
C.count=100#类的属性是与类的对象进行绑定的，不会依赖它任何实例对象
print(a.count,b.count)

#属性名跟方法名相同，属性会覆盖方法
class B:
    def x(self):
        print('Xman')
d=B()
print(d.x())
d.x=1
print(d.x)
#print(d.x()) 被方法被属性覆盖

'''
绑定
'''
class BB:
    def printBB():
        print("WZS")
print(BB.printBB())

#self作用：对象的方法被调用时，对象会将自身的引用作为第一个参数传给该方法
#没有self,bb对象作为第一个参数传入，出错
bb=BB()
print(bb.printBB())


#__dict__属性由字典组成，字典中仅有的实例对象的属性
#不显示类属性和特殊属性。键表示属性名，值表示属性相应的数据值
class CC:
    def setXY(self,x,y):
        self.x=x
        self.y=y
    def printXY(self):
        print(self.x,self.y)
dd=CC()
print(dd.__dict__) #显示{}
dd.setXY(4,5)#None
print(dd.printXY())
print(dd.__dict__)#{'x': 4, 'y': 5}

del CC #删除类
print(dd.printXY())



'''
实例
'''

class Person: # 定义一个人类
    role = 'person' # 人的角色属性都是人
    def __init__(self, name, aggressivity, life_value):
        self.name = name # 每一个角色都有自己的昵称;
        self.aggressivity = aggressivity # 每一个角色都有自己的攻击力;
        self.life_value = life_value # 每一个角色都有自己的生命值;

    def attack(self, dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.aggressivity


class Dog: # 定义一个狗类
    role = 'dog' # 狗的角色属性都是狗
    def __init__(self, name, breed, aggressivity, life_value):
        self.name = name # 每一只狗都有自己的昵称;
        self.breed = breed # 每一只狗都有自己的品种;
        self.aggressivity = aggressivity # 每一只狗都有自己的攻击力;
        self.life_value = life_value # 每一只狗都有自己的生命值;
    def bite(self,people):
        # 狗可以咬人，这里的狗也是一个对象。
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
        people.life_value -= self.aggressivity

egg = Person('egon',10,1000) #创造了一个实实在在的人egg
ha2 = Dog('二愣子','哈士奇',10,1000) #创造了一只实实在在的狗ha2
print(ha2.life_value) #看看ha2的生命值
egg.attack(ha2) #egg打了ha2一下
print(ha2.life_value) #ha2掉了10点血


'''继承'''
#=======================
class Animal:
    '''
    人和狗都是动物，所以创造一个Animal基类
    '''
    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity  # 人和狗都有自己的攻击力;
        self.life_value = life_value  # 人和狗都有自己的生命值;
    def eat(self):
        print('%s is eating' % self.name)


class Dog(Animal):
    '''
    狗类，继承Animal类
    '''
    def bite(self, people):
        '''
        派生：狗有咬人的技能
        :param people:
        '''
        people.life_value -= self.aggressivity


class Person(Animal):
    '''
    人类，继承Animal
    '''
    def attack(self, dog):
        '''
        派生：人有攻击的技能
        :param dog:
        '''
        dog.life_value -= self.aggressivity
egg = Person('egon', 10, 1000)
ha2 = Dog('二愣子', 50, 1000)
print(ha2.life_value)
print(egg.attack(ha2))
print(ha2.life_value)

#=======================
from math import pi
class O:
    '''
    定义了一个圆形类；
    提供计算面积(area)和周长(perimeter)的方法
    '''
    def __init__(self,long):
        self.long=long

    def area(self):
        return pi * self.long * self.long

    def perimeter(self):
        return 2 * pi * self.long
o=O(10)
area1=o.area()
perimeter1=o.perimeter()
print(area1,perimeter1)

'''组合'''
#=====================================
''''''
class Person: # 定义一个人类
    role = 'person' # 人的角色属性都是人
    def __init__(self, name, aggressivity, life_value, money):
        self.name = name # 每一个角色都有自己的昵称;
        self.aggressivity = aggressivity # 每一个角色都有自己的攻击力;
        self.life_value = life_value # 每一个角色都有自己的生命值;
        self.money = money
    def attack(self,dog):
        # 人可以攻击狗，这里的狗也是一个对象。
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.aggressivity

class Dog: # 定义一个狗类
    role = 'dog' # 狗的角色属性都是狗
    def __init__(self, name, breed, aggressivity, life_value):
        self.name = name # 每一只狗都有自己的昵称;
        self.breed = breed # 每一只狗都有自己的品种;
        self.aggressivity = aggressivity # 每一只狗都有自己的攻击力;
        self.life_value = life_value # 每一只狗都有自己的生命值;
    def bite(self,people):
        # 狗可以咬人，这里的狗也是一个对象。
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
        people.life_value -= self.aggressivity


class Weapon: #装备
    def __init__(self,name, price, aggrev, life_value):
        self.name = name
        self.price = price
        self.aggrev = aggrev
        self.life_value = life_value
    def update(self, obj): #obj就是要带这个装备的人
        obj.money -= self.price # 用这个武器的人花钱买所以对应的钱要减少
        obj.aggressivity += self.aggrev # 带上这个装备可以让人增加攻击
        obj.life_value += self.life_value # 带上这个装备可以让人增加生命值
    def prick(self, obj): # 这是该装备的主动技能,扎死对方
        obj.life_value -= 500 # 假设攻击力是500

lance = Weapon('长矛',200,6,100)
egg = Person('egon',10,1000,600) #创造了一个实实在在的人egg
ha2 = Dog('二愣子','哈士奇',10,1000) #创造了一只实实在在的狗ha2

#egg独自力战"二愣子"深感吃力，决定穷毕生积蓄买一把武器
if egg.money > lance.price: #如果egg的钱比装备的价格多，可以买一把长矛
    lance.update(egg) #egg花钱买了一个长矛防身，且自身属性得到了提高
    egg.weapon = lance #egg装备上了长矛

print(egg.money,egg.life_value,egg.aggressivity)
print(ha2.life_value)
egg.attack(ha2) #egg打了ha2一下
print(ha2.life_value)
egg.weapon.prick(ha2) #发动武器技能
print(ha2.life_value) #ha2不敌狡猾的人类用武器取胜，血槽空了一半

'''组合'''
#=============================

from math import pi
class Circle:
    '''
    定义了一个圆形类；
    提供计算面积(area)和周长(perimeter)的方法
    '''
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * self.radius * self.radius
    def perimeter(self):
        return 2 * pi *self.radius
circle = Circle(10) #实例化一个圆
area1 = circle.area() #计算圆面积
per1 = circle.perimeter() #计算圆周长
print(area1,per1) #打印圆面积和周长

class Ring:
    '''
    定义了一个圆环类
    提供圆环的面积和周长的方法
    '''
    def __init__(self,radius_outside,radius_inside):
        self.outsid_circle = Circle(radius_outside)
        self.inside_circle = Circle(radius_inside)

    def area(self):
        return self.outsid_circle.area() - self.inside_circle.area()

    def perimeter(self):
        return self.outsid_circle.perimeter() + self.inside_circle.perimeter()

ring = Ring(10,5) #实例化一个环形
print(ring.perimeter()) #计算环形的周长
print(ring.area()) #计算环形的面积

'''组合'''
#============================
class BirthDate:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

class Couse:
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period

class Teacher:
    def __init__(self,name,gender,birth,course):
        self.name=name
        self.gender=gender
        self.birth=birth
        self.course=course

def teach(self):
    print('teaching')

p1=Teacher('egon','male',
BirthDate('1995','1','27'),
Couse('python','28000','4 months')
)
print(p1.birth.year,p1.birth.month,p1.birth.day)
print(p1.course.name,p1.course.price,p1.course.period)


'''继承'''
#=======================
class Animal:
    def eat(self):
        print("%s 吃 " %self.name)
    def drink(self):
        print ("%s 喝 " %self.name)

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.breed = '猫'
    def climb(self):
        print('爬树')

class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.breed='狗'
    def look_after_house(self):
        print('汪汪叫')

c1 = Cat('小白家的小黑猫')
c1.eat()
c2 = Cat('小黑的小白猫')
c2.drink()
d1 = Dog('胖子家的小瘦狗')
d1.eat()


'''继承'''
#=======================
class Animal:
    def __init__(self, name, aggressivity, life_value):
        self.name = name # 人和狗都有自己的昵称;
        self.aggressivity = aggressivity # 人和狗都有自己的攻击力;
        self.life_value = life_value # 人和狗都有自己的生命值;
    def eat(self):
        print('%s is eating' % self.name)

class Dog(Animal):
    pass

class Person(Animal):
    pass

egg = Person('egon', 10, 1000)
ha2 = Dog('二愣子', 50, 1000)
egg.eat()
ha2.eat()


