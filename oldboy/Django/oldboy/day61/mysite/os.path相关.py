import os

ret = os.path.abspath(__file__)
print(ret)

ret2=os.path.dirname(os.path.abspath(__file__))
print(ret2)

ret3=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ret3)


#os.path.join拼接
ret4=os.path.join(ret3,"templates")
print(ret4)