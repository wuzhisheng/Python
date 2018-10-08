#在循环一个列表时，不要改变列表的大小，否则结果会报错或者出错
#去除列表偶数
li=[1,2,3,4,5,6,7,8,9]
#(一)
del li[1::2]
print (li)

#(二)
new_li=[]
for index in range(len(li)):
    if index % 2 == 0:
         new_li.append(li[index])
li=new_li
print(li)

#（三）
for index in range(len(li)-1,-1,-1):
    if index % 2 == 1:
        del li[index]
print(li)


#会报错
#(1)
# for i in range(len(li)):
#     if i%2 == 1:
#         del li[i]
# print(li)

#(2)
# for index in range(len(li)):
#     print(index)
#     print(li)
#     if index % 2 == 1:
#         del li[index]
#     print(index)
#     print(li)



#在循环一个字典时，不要改变字典的大小，这样结果会报错
dic={'k1':'v1','k2':'v2','name':'wu'}
list=[]
for key in dic:
    if 'k' in key:
        list.append(key)
# print (list)
for index in list:
    del dic[index]
print(dic)





