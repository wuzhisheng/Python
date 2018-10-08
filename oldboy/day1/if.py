''''''
'''
if
if 条件：
条件成立，则执行下一步
'''
#True 可改成3>2
 #1
if True:
    print('2222')

 #2
if False:
    print('333')
else:
    print('444')

wu=False
if wu:
    print('true')
else:
    print('false')

 #3
if 2 < 1:
    print ('false')
elif 4 > 3:
    print ('ture1')
elif  4 > 1:
    print('ture2')

#input输入的是字符串
# =是赋值  ==是比较
# !=  是否不等
num= int(input('输入数字：'))
if num <=10  and num >= 1:
    print(num)
else:
    print("hahhah")

num=input('请输入数字：')
if num == '1':
    print('数字为1')
elif num== '2':
    print('数字为2')
elif num== '3':
    print('数字为3')

#if ... elif...else:
#流程控制只会执行一个条件
wu = int(input('请输入分数：'))
if wu >= 90:
    print('成绩为A')
elif wu >= 80:
    print ('成绩为B')
elif wu >= 60:
    print('成绩为C')
else:
    print('成绩为D')


#if嵌套
name=input('请输入姓名：')
password=input('请输入密码：')
if name == "wzs":
    if password == '1234':
        print ('密码正确')
    else:
        print ('密码错误')
else:
    print ('用户名错误')

#确定列表不是空的
lists = []
if lists:
	for list in lists:
		print("Adding " + list + ".")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

'''
其中第一个列表包含比萨店供应的配料，
而第二个列表包含顾客点的配料。这次对于requested_toppings中的
每个元素，都检查它是否是比萨店供应的配料，再决定是否在比萨中添加它：
'''

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
	    print("Adding " + requested_topping + ".")
    else:
		print("Sorry, we don't have " + requested_topping + ".")
		print("\nFinished making your pizza!")