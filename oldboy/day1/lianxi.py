name="wzs"
password=123
time=3
wallet={}
while time >= 1:
    user =input("请输入用户名：")
    passwd=int(input("请输入密码"))
    if user == name and passwd == password:
        print("登录成功")
        n1=input("您好"+name+"先生/女士，您是否充值Y|N").upper()
        if n1 == "Y":
            n2=int(input("请输入充值金额："))
            wallet['name']=n2
            print("充值成功")
            break
        else:
            continue
    else:
        time -=1
        print("登录失败，您还有",time,"次机会")
        continue