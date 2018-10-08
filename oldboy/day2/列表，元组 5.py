'''
[头：尾：隔和方向]
'''
'''
列表由一系列按特定顺序排列的元素组成
元素之间可以没有任何关系
用方括号（[]）来表示列表，并用逗号来分隔其中的元素

索引从 0 而不是 1 开始
'''

l=['wu',[1,2,3],'oldboy']
#打印
print(s1=l[0]) #显示第一个
print(l[-1]) #显示倒数第一个
print (l[:2])
print (l[:]) #显示全部
print(l[:3:2]) #不显示第2个

l=['wu',[1,2,3],'oldboy']
#增
    #append 追加
l.append('zhi')
print(l)
    #extend 迭代着追加
l.extend('alex')
print(l)
    #insert 插入
l.insert(3,'sheng')
print(l)
    # +,两个list相加会得到新的list
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
l2=[1,"a",3,4,"heart"]
l3=li+l2
print(l3)

l=['wu',[1,2,3],'oldboy']
#删
     #pop按照索引删除，有返回值
     #返回删除的值
print(l.pop(1)) #删除第二个元素
     #remove 按照元素删除
    #删除错误会报错
l.remove('oldboy')
print(l)
   #clear() 清空列表
l.clear()
print(l)
    #del
        #1.按照索引删除
del l[0]
print (l)
        #2.按照切片（步长）删除
del l[:3]
print (l)
del l[::2]
print (l)
        #3.删除整个列表
del l
print (l)


l=['wu',[1,2,3],'oldboy','hai','asd']
#改
    #按照索引修改
l[0]='zhi'
print(l[0])
    #按照切片修改
l[:2]='qwer' #将l 列表前2个元素去掉换成'qwer'
print (l)
    #按照切片+步长去改
l[::2] = [1,2,3] #以间隔2，按顺序修改列表
l[::2] = 'asc'
print(l)

print(l[-2:]) #打印最后三名

# 列表查
    # for循环查
l = [1, 1, 4, 3, 6, 5]
for i in l:
    print(i)
    #count
print (l.count(1))
    #len #统计长度
print(len(l))
    #sort #从小到大
    #sorted对列表进行临时排序
l.sort() #永久性地修改了列表元素的排列顺序
print (l)
    #reverse #从大到小  永久性地修改列表元素的排列顺序
    #但是在重复使用一次则恢复原来顺序
l.reverse()
print (l)

'''
操作列表
'''

l=['wu','zhi','sheng']
for i in l:
    print(l.index(i)) #显示索引位置 0,1,2

for i in l: #遍历list元素
    print(l)

for q in range(len(l)):
    print (q)

'''
range 要结合for循环
'''
number=list(range(1,6))
print(number)

for i in range(1, 11):
    print(i)

for q in range(1, 11, 2):
     print(q)

for w in range(10, -1, -1):
    print(w)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)
'''
l1 = ['wusir', 'alex', [1,'taibai','ritian'],12]
# 将列表中的alex 首字母大写。
# 给[1,'taibai','ritian'] 追加一个值：景丽洋。
# 将列表中的太白：全部大写。
# 讲 数字 1 通过数字相加方式变成 100.
'''
l1 = ['wusir', 'alex', [1,'taibai','ritian'],12]
l1[1]=l1[1].capitalize() #修改要重新定义变量
print (l1)

l1[2].append('景丽洋')  #增加不用
print (l1)

l1[2][1]=l1[2][1].upper()
print(l1)

l1[2][0] +=99
print(l1)

'''
元组 tuple ：只读列表（放一些重要数据类型，只有读权限）
'''


tul=(1,'alex',[1,2,3],{'name':'alex'},True)
print(tul[1]) #显示字符串
print(tul[:3]) #显示元组

for i in tul:
    print(i)
#儿子不能改，孙子可以改
tul[2].append(666)
print(tul)

del tul[2]
print(tul)

tul[3].clear()
print(tul)
