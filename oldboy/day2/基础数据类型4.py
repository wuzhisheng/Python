''''''
'''
字符串：str
存储少量数据类型
python中：凡是用单/双引号引起来的数据就是字符串。
str = 'wuzhisheng   吴志盛'
str1 = "wuzhisheng   吴志盛"
wu='''
'''

# """ """或'''  ''' 保留格式

字符串可以用 + 或 *
+ 将字符串进行拼接

w = 'wu'
z = 'zhi'
# 加可以 
print(w + z)
print(w * 3)

切片：
w="wwww"
print(w[::2])
'''


#capitalize()首字母大写，其余小写 **
s1='oldBoy'
s2=s1.capitalize()
print (s2)

#swapcase 大小写转换 **
s1='oldBoy'
print (s1.swapcase())


#title() 对字符串非字母隔开的每个单词首字母大写**
s1='alex oldboy*tai2tian'
print(s1.title())

#upper  全部转换为大写  *****
# lower  全部转换为小写
# s1='oldBoy'
# print (s1.upper())
# #应用场景
# username=input("用户名：")
# password=input("密码：")
# code = 'QweR'.upper()
# your_code=input('验证码').upper()
# if  code == your_code:
#     if username == 'alex' and password=='123':
#          print('登录成功')
# else:
#     print('验证失败')



#strip 默认去除字符串前后两端的空格，换行符，制表符*****
#可指定去除某和某些元素  ????
#lstrip() rstrip()
name='  alex  '
print(name.strip()) #这种删除只是暂时的
#要永久删除这个字符串中的空白，必须将删除操作的结果存回到变量中
name1=name.strip()

n1=' :aldydtojhgld'
print(n1.strip('ald'))
print(n1.strip(':'))


#startswith endswith *****判断以...开头....结尾
s1='oldBoy'
print(s1.startswith('o'))
print(s1.startswith('old'))
print(s1.startswith('B',3,))
s1.endswith

s1='oldBoyB'
#find 通过字符串元素找索引，找不到返回-1 *****
#index 通过字符串元素找索引，找不到会报错
print (s1.index('B'))
print (s1.index('B',4)) #4查找范围
# print (s1.index('A')) #找不到，会报错
# print (s1.find('A')) #找不到返回-1
i=(s1.index('B'))
print(i,type(i))

#split 分割 str ---> list 默认以空格分隔 *****
#分割后以列表显示
s1='wu zhi sheng'
s2='wu,zhi,sheng'
s3='wuzhisheng'
print (s1.split())
print (s2.split(','))
print(s3.split('w',1)) #切第一个，则会流空格


#replace 替换*****
s1='alex是一个sg,alex确实是，alex'
print(s1.replace('alex','oldboy'))
print(s1.replace('alex','oldboy',2)) #2指定替换个数
print(s1.replace('wu','oldboy'))#不存在，打印原来的，但没报错


#format 三种用法
    #1
msg='我们{}，今年{}，性别{}'.format('wu',25,'男')
print (msg)
    #2
msg='我们{0}，今年{1}，性别{0}'.format('wu',25,'男')
print (msg)
    #3
msg='我们{name}，今年{age}，性别{sex}'.format(name='wu',sex='男',age=25)
print(msg)


#count 查询元素出现的次数
s1='oldBoyB'
print(s1.count('B'))
#len 显示长度
print(len(s1))


name='wuzhi123'
print(name.isalnum()) #判断字符串是否由字母或数字组成
print (name.isalpha()) #判断字符串是否只由字母组成
print (name.isdigit())  #判断字符串是否只由数字组成


#join 将序列中的元素以指定的字符连接生成一个新的字符串
lst = ['alex','alex3714']
ret = '|'.join(lst)
print(ret)

str='-'
seq=("a","b","c")
print (str.join(seq))

#eval 去掉字符串，转换相应数据类型
l = '[1,2,3,4,[5,6,7,8,9]]'
d = "{'a':123,'b':456,'c':789}"
t = '([1,3,5],[5,6,7,8,9],[123,456,789])'
print(type(l))
print(type(eval(l)))
print(eval(l))

print(type(d))
print(type(eval(d)))
print(eval(d))

print(type(t))
print(type(eval(t)))
print(eval(t))


#while:无限循环，强调次数
s1='oldboy'
index=0
while index < len(s1):
    print(s1[index])
    index+=1

#for 有限循环，遍历存在的对象
'''
for循环可以与else配合，与break和continue
'''
s1='oldboy'
for i in s1:
    print(i)
    #break
    #continue
else:
    pass

