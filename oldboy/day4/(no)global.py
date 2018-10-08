#global 修改全局变量
num=5
def fun():
    global num
    num=10
    print(num)
fun()