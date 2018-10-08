'''else 使用'''
'''
if 条件:
    条件为真执行
else:
    条件为假执行
'''
#for或while 干完怎么样，干不完就别想怎样
'''
//  只显示个整数
%   只显示余数
用户所输入数是素数，则显示素数 否则显示最大约数，
'''
def maxfactor(num):
    count=num//2
    while count > 1:
        if num % count == 0:
            print('%d 最大的约数是%d' % (num,count))
            break
        count-=1
    else:
        print ('%d 是素数！'% num)
num=int(input('请输入一个数'))
maxfactor(num)

#没有问题？那就干吧
try:
    int('asd')
except ValueError as reason:
    print('出错啦'+str(reason))
else:
    print('没有任何异常')