
#zip()函数
a=['1','2']
b=['a','b']
d=zip(a,b)
print(dict(d))
#{'1': '2', 'a': 'b'}

#使用嵌套列表转换为字典
a=['1','2']
b=['a','b']
c=[a,b]
print(dict(c))
dic={}
for i in c:
    dic[i[0]]=i[1]
print (dic)
#{'1': '2', 'a': 'b'}

# #zip()函数
lis=['a','b','1','2']
b=dict(zip(lis[0::2],lis[1::2]))
print(b)

dic={}
for i in range(0,len(lis),2):
    b[[i]]






