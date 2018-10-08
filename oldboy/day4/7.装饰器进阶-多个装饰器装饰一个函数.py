# 登陆login、计算时间timer
# @login
# @timer
# def select():
#     pass

#
# # 计算时间
# def delete():
#     pass

def wrapper1(func):              # func = inner2
    def inner1(*args,**kwargs):
        print('wrapper1 before')
        ret = func(*args,**kwargs)  # inner2()
        print('wrapper1 after')
        return ret
    return inner1

def wrapper2(func):                 # func = qqxing
    def inner2(*args,**kwargs):
        print('wrapper2 before')
        ret = func(*args,**kwargs)  # qqxing
        print('wrapper2 after')
        return ret
    return inner2

@wrapper1       # qqxing = wrapper1(qqxing)  ==> wrapper1(wrapper2(qqxing)) ==> wrapper1(inner2) ==> inner1
@wrapper2       # qqxing = wrapper2(qqxing)
def qqxing():
    print('---qqxing---')

qqxing()        # inner1

