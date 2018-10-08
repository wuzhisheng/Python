''''''
'''
dic{key:value..}
字典可以存储大量的数据类型，而且可以存储关系型数据。是python唯一映射数据类型
其key，必须是不可变的数据,int,str,bool,tuple
可变的数据类型,list,dict,set
字典的值任意类型
字典的key是不重复
字典：3.5包括3.5版本之前，无序
字典：3.6之后有序
'''
dic={'name':'wu','age':100}
#增
    #dic[key]=value 有则改，无则加
#无则加
dic['sex']='men'
print(dic)
#有则改
dic['name']='hai'
print(dic)
    #setdeafult
dic.setdefault('sex') #有则不变，无则加
dic.setdefault('sex','men')
print (dic)
    #update 增加
dic.update(a=66,b=77,c=22)
print (dic)

#删
    #pop
print(dic.pop('name')) #会显示删除的值
print(dic.pop('name1','无此键')) #显示无此键
print (dic)
    #popitem
#poptiem 3.6删除最后一个3.5之前随机删除，有返回值
print(dic.popitem()) #删除末尾
print (dic)
    #clear()清空
dic.clear()
print(dic)
    #del
#按照键删除键值对
del dic['name']
print(dic)

#查
    #按键查
print(dic['name']) #判断是否存在 ,有则返回values,无则报错
print(dic.get('name')) #判断是否存在,有则返回values,无则显示None

#dic.keys()
#dic.values()
#dic.items()
for key in dic.keys():
    print(key)
#或者
for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key,value in dic.items():
    print(key,value)

#显示1，2,3为键，alex为值
dic=dict.fromkeys([1,2,3],'alex')
print(dic)




'''
dic = {'name_list':['张三','李四'],1:{'name':'alex','age':1000,2:[1,2,3]}}
# 给['张三','李四'] 张三后面插入一个元素：王五。
# 将李四变成lisi.
# 将name对应的alex变成大写。
# 将2 对应的列表中的3删除。
'''
dic = {'name_list':['张三','李四'],1:{'name':'alex','age':1000,2:[1,2,3]}}
# print(dic['name_list'])
dic['name_list'].insert(1,'王五')
print(dic)

# l2=dic['name_list']
# l2[2]='lisi'
# print(dic)
dic['name_list'][-1]='lishi'
print(dic)


# print(dic[1]['name'].upper())
dic[1]['name']=dic[1]['name'].upper()
print (dic)

# print(dic[1][2])
dic[1][2].pop()
print (dic)
