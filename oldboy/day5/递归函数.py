''''''
#递归的最大深度—997
def foo(n):
    print(n)
    n += 1
    foo(n)
foo(1) #显示到998结束
#这是python3保护层
#以下可以设置成100000层
import sys
print(sys.setrecursionlimit(100000))



def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
number=int(input("请输入个整数："))
result=fact(number)
print("%s的阶乘是%s" % (number,result))
