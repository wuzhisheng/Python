# 循环
    # while循环 ：不知道具体要循环多少次
        # 死循环 无限循环
        # 满足条件才推出
    # for循环 ： 知道要循环的次数
        # for i in range(100)
        # for i in list/tuple/dict/str

"""
while 条件：
循环体
"""
#无限循环
while True:
    print ('wu')
    print ('zhi')
    print ('name')

'''
终止循环的方是方式
1.改变条件
2.break：只要遇到break，就立马跳出循环体
'''

#循环是先走到底再会来判断条件
flag=True
while flag:
    print ('wu')
    print('sheng')
    flag=False
    print('zhi')

num=1
while  num <= 100:
    print (num)
    num=num+1

#1.领一个数从1到100
#2.领一个数相加
num=1
s=0
while  num <= 100:
    s=s+num
    num=num+1
print (s)

#break 只要遇到break，就立马跳出循环体
while True:
    print ('wu')
    print('sheng')
    break
    print('zhi')

#continue 立马跳回while开头重新开始
while True:
    print ('wu')
    print('sheng')
    continue
    print('zhi')

#while else:当while循环被break终止时，不会执行else
count=1
while count < 5:
    if count >= 3:
        print(count)
    count=count+1
else:
    print('循环结束...')
print(6666)


count=1
while count < 5:
    if count >= 3:
        break
    count=count+1
else:
    print('循环结束...')
print(6666)
