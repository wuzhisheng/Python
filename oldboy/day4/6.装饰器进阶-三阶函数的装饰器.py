# 给装饰器传参数
    # 从装饰器的外部来控制装饰器内部的逻辑的时候
#带参数的装饰器
# flask框架
flag = False
import time
def outer(flag):
    def cal_time(func):
        def inner(*args,**kwargs):
            if flag:
                start = time.time()
                ret = func(*args,**kwargs)
                print(time.time() - start)
            else:
                ret = func(*args, **kwargs)
            return ret
        return inner
    return cal_time

@outer(flag)   # ==> outer(True) = cal_time = @cal_time
def func():
    time.sleep(0.1)
    print('in func')

@outer(flag)
def wahaha():
    time.sleep(0.1)
    print('in wahaha')

@outer(True)
def qqxing():
    time.sleep(0.1)
    print('in qqxing')

@outer(flag)
def xuebi():
    time.sleep(0.1)
    print('in xuebi')
func()
qqxing()
wahaha()