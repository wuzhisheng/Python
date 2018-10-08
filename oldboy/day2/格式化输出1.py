#格式化输出
'''
应用：想要字符串的某些位置变成动态的
'''
#（1）
name=input("名字：")
sex=input("性别：")
job=int(input("身高："))
hobby=input("爱好：")
#%占位符 s字符串  d数字  f浮点数
information='''
name%s
sex:%s
high:%d
hobby:%s
''' %(name,sex,job,hobby)
print(information)


#（3）
dict = {'name':'wu','sex':'man','high':'188','hobby':'haha'}
information='''
name%(name)s
sex:%(sex)s
high:%(high)s
hobby:%(hobby)s
''' % dict
print(information)

#（3）
s1='我是%s,爱好%s,输出2%%' % ('wu','篮球')
print (s1)

#for 会遍历字符串每个元素
num="wzs"
for i in num:
    print(i)