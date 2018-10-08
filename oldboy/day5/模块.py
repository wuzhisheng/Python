''''''
'''
import 导入模块
第一次导入后就将模块名加载到内存，
后续重复导入只是引用，不会重新执行模块内

import my_module as sm #为my_module命名为sm

'''

'''
模块：包含了python定义和声明的文件

import加载的模块分为四个通用类别：
1 使用python编写的代码（.py文件）
2 已被编译为共享库或DLL的C或C++扩展
3 包好一组模块的包
4 使用C编写并链接到python解释器的内置模块
'''
'''
random模块
'''
#随机小数
import random
random.random() # 大于0且小于1之间的小数
random.uniform(1,3) #大于1小于3的小数

#随机整数
random.randint(1,5) # 大于等于1且小于等于5之间的整数
random.randrange(1,10,2) # 大于等于1且小于10之间的奇数

#随机选择一个返回
random.choice([1,'23',[4,5]]) # #1或者23或者[4,5]
#随机选择多个返回，返回的个数为函数的第二个参数
random.sample([1,'23',[4,5]],2) # #列表元素任意2个组合

#打乱列表顺序
item=[1,3,5,7,9]
random.shuffle(item) # 打乱次序
print(item)


'''
collections模块
'''
from collections import namedtuple
#namedtuple('名称', [属性list]):
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)


#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
#appendleft()和popleft()


#OrderedDict()
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print (d) # dict的Key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od) # OrderedDict的Key是有序的

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od.keys()) # 按照插入的Key的顺序返回


#defaultdict:作用key不存在时，返回一个默认值
from collections import defaultdict
values = [11,22,33,44,55,66,77,88,99,90]
my_dict = defaultdict(list)
for value in values:
    if value>66:
        my_dict['k1'].append(value)
    else:
        my_dict['k2'].append(value)
print(my_dict)

from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1']) # key1存在
print(dd['key2']) # key2不存在，返回默认值

#Counter
#跟踪值出现的次数,是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value
from collections import Counter
c = Counter('abcdeabcdabcaba')
print (c)


'''
时间模块
'''
import time
#常用方法
# 1.time.sleep(secs)
# (线程)推迟指定的时间运行。单位为秒。
# 2.time.time()
# 获取当前时间戳

    #导入时间模块
import time
    #时间戳
print(time.time())

    #时间字符串
print(time.strftime("%Y-%m-%d %X"))
print(time.strftime("%Y-%m-%d %H-%M-%S"))

        #时间元组:localtime将一个时间戳转换为当前时区的struct_time
print(time.localtime())

        #time.ctime(时间戳)  --> %a %b %d %H:%M:%S %Y串
print(time.ctime())
print(time.ctime(1500000000))
        #结构化时间 --> %a %b %d %H:%M:%S %Y串
print(time.asctime())
print(time.localtime(1500000000))





'''
os模块
'''
import os
os.makedirs('dirname1/dirname2')#可生成多层递归目录
os.removedirs('dirname1')#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')#生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')#删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()#删除一个文件
os.rename("oldname","newname")#重命名文件/目录
os.stat('path/filename')#获取文件/目录信息
os.system("bash command")#运行shell命令，直接显示
os.popen("bash command).read()")#运行shell命令，获取执行结果
os.getcwd()#获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")#改变当前脚本工作目录；相当于shell下cd os.path
os.path.abspath("path")#返回path规范化的绝对路径
os.path.split("path")#将path分割成目录和文件名二元组返回
os.path.dirname("path")#返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename("path")#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists("path")#如果path存在，返回True；如果path不存在，返回False
os.path.isabs("path")#如果path是绝对路径，返回True
os.path.isfile("path")#如果path是一个存在的文件，返回True。否则返回False
os.path.isdir("path")#如果path是一个存在的目录，则返回True。否则返回False
os.path.join("path1[, path2[, ...]]")#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime("path")#返回path所指向的文件或者目录的最后访问时间
os.path.getmtime("path")#返回path所指向的文件或者目录的最后修改时间
os.path.getsize("path")#返回path的大小



'''
序列化
将原本的字典、列表等内容转换成一个字符串的过程
将字典转换成一个字符串很简单，可用str(dic)   ==》序列化（数据结构=》str）
eval()可将字符串转换成字典 ==》反序列化（str==》数据结构）
将字符串str当成有效的表达式来求值并返回计算结果
安全性是其最大的缺点
例如：如果我们从文件中读出的不是一个数据结构，而是一句"删除文件"类似的破坏性语句


作用
问题：python代码中计算的一个数据需要给另外一段程序使用
解决：存在文件，但文件件只识别字符串
'''
'''
Json模块提供了四个功能：dumps、dump、loads、load
'''
import json
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = json.dumps(dic) #序列化：将一个字典转换成一个字符串
print(type(str_dic),str_dic) #<class 'str'> {"k3": "v3", "k1": "v1", "k2": "v2"}
#注意，json转换完的字符串类型的字典中的字符串是由""表示的
dic2 = json.loads(str_dic) #反序列化：将一个字符串格式的字典转换成一个字典
#注意，要用json的loads功能处理的字符串类型的字典中的字符串必须由""表示
print(type(dic2),dic2) #<class 'dict'> {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

import json
f = open('json_file','w')
dic = {'k1':'v1','k2':'v2','k3':'v3'}
json.dump(dic,f) #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
f.close()

f = open('json_file')
dic2 = json.load(f) #load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
f.close()
print(type(dic2),dic2)

'''
用于序列化的两个模块
json，用于字符串 和 python数据类型间进行转换
pickle，用于python特有的类型 和 python的数据类型间进行转换

dumps、dump(序列化，存）、loads（反序列化，读）、load （不仅可以序列化字典，列
表...可以把python中任意的数据类型序列化）
'''


'''
pickle
提供了四个功能：dumps、dump(序列化，存）、loads（反序列化，读）、load （不仅可以序列化字典，列
表...可以把python中任意的数据类型序列化）
'''
import pickle
dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle.dumps(dic)
print(str_dic) #一串二进制内容

dic2 = pickle.loads(str_dic)
print(dic2) #字典

import time
struct_time = time.localtime(1000000000)
print(struct_time)
f = open('pickle_file','wb')
pickle.dump(struct_time,f)
f.close()

f = open('pickle_file','rb')
struct_time2 = pickle.load(f)
print(struct_time2.tm_year)

'''
用于序列化的两个模块
json，用于字符串 和 python数据类型间进行转换
pickle，用于python特有的类型 和 python的数据类型间进行转换

json是一种所有的语言都可以识别的数据结构。
如果我们将一个字典或者序列化成了一个json存在文件里，那么java代码或者js代码也可以拿来用。
但是如果我们用pickle进行序列化，其他语言就不能读懂这是什么了～
所以，如果你序列化的内容是列表或者字典，我们非常推荐你使用json模块
但如果出于某种原因你不得不序列化其他的数据类型，而未来你还会用python对这个数据进行反序列化的话，那么就可
以使用pickle
'''



'''
[0-9] 
[a-z] 
[A-Z] 
[0-9a-fA-F]


字符：
=====================
. 匹配除换行符以外的任意字符
\w 匹配字母或数字或下划线
\s 匹配任意的空白符
\d 匹配数字
\n 匹配一个换行符
\t 匹配一个制表符
\b 匹配一个单词的结尾
^ 匹配字符串的开始
$ 匹配字符串的结尾
\W 匹配非字母或数字或下划线
\D 匹配非数字
\S 匹配非空白符
a|b 匹配字符a或字符b
() 匹配括号内的表达式，也表示一个组
[...] 匹配字符组中的字符
[^...] 匹配除了字符组中字符的所有字符

量词：
======================
* 重复零次或更多次
+ 重复一次或更多次
? 重复零次或一次
{n} 重复n次
{n,} 重复n次或更多次
{n,m} 重复n到m次
'''
import re
phone_number = input('please input your phone number ： ')
if re.match('^(13|14|15|17|18)[0-9]{9}$',phone_number):
    print('是合法的手机号码')
else:
    print('不是合法的手机号码')


import re
ret = re.findall('a', 'eva egon yuan') # 返回所有满足匹配条件的结果,放在列表里
print(ret) #结果 : ['a', 'a']

ret = re.search('a', 'eva egon yuan').group()
print(ret) #结果 : 'a'
# 函数会在字符串内查找模式匹配,只到找到第一个匹配然后返回一个包含匹配信息的对象,该对象可以
# 通过调用group()方法得到匹配的字符串,如果字符串没有匹配，则返回None。

ret = re.match('a', 'abc').group() # 同search,不过尽在字符串开始处进行匹配
print(ret)
#结果 : 'a'

ret = re.split('[ab]', 'abcd') # 先按'a'分割得到''和'bcd',在对''和'bcd'分别按'b'分割
print(ret) # ['', '', 'cd']

ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)#将数字替换成'H'，参数1表示只替换1个
print(ret) #evaHegon4yuan4

ret = re.subn('\d', 'H', 'eva3egon4yuan4')#将数字替换成'H'，返回元组(替换的结果,替换了多少次)
print(ret)

obj = re.compile('\d{3}') #将正则表达式编译成为一个 正则表达式对象，规则要匹配的是3个数字
ret = obj.search('abc123eeee') #正则表达式对象调用search，参数为待匹配的字符串
print(ret.group()) #结果 ： 123

ret = re.finditer('\d', 'ds3sy4784a') #finditer返回一个存放匹配结果的迭代器
print(ret) # <callable_iterator object at 0x10195f940>
print(next(ret).group()) #查看第一个结果
print(next(ret).group()) #查看第二个结果
print([i.group() for i in ret]) #查看剩余的左右结果

#1 findall的优先级查询：
ret = re.findall('www.(baidu|oldboy).com', 'www.oldboy.com')
print(ret) # ['oldboy'] 这是因为findall会优先把匹配结果组里内容返回,如果想要匹配结果,取消权限即可
ret = re.findall('www.(?:baidu|oldboy).com', 'www.oldboy.com')
print(ret) # ['www.oldboy.com']

#2 split的优先级查询
ret=re.split("\d+","eva3egon4yuan")
print(ret) #结果 ： ['eva', 'egon', 'yuan']

ret=re.split("(\d+)","eva3egon4yuan")
print(ret) #结果 ： ['eva', '3', 'egon', '4', 'yuan']
#在匹配部分加上（）之后所切出的结果是不同的，
#没有（）的没有保留所匹配的项，但是有（）的却能够保留了匹配的项