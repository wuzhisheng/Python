user_status={
    "username":None,
    "status":False
}
dic1={
    1: '登录',
    2: '注册',
    3: '文章',
    4: '日记',
    5: '评论',
    6: '收藏',
    8: '退出程序'
}

dic2={
    3: 'artecle',
    4: 'diary',
    5: 'comment',
    6: 'collection',
    7: 'logout',
    8: 'exited'
}

def wrapper(f1):
    def inner(*args,**kwargs):
        if user_status["status"]:
            set = f1(*args, **kwargs)
        else:
            print("请登录")
            login()
    return inner


def login():
    cot=2
    while cot >=0:
        usernm=input("username:").strip()
        passwd=input("password:").strip()
        with open("register",mode="r",encoding="utf-8") as f1:
            for line in f1:
                if line.split()[0] == usernm and line.split()[1] == passwd:
                    print("登录成功")
                    cot=-1
                    global user_status
                    user_status["status"]=True
            else:
                print("error,你还有%s次机会" % cot)
                cot-=1


def register():
    print("请您注册用户信息")
    usernm1=input("username1:").strip()
    with open('register',mode="r+",encoding="utf-8") as f1:
        for line in f1:
            if line.split()[0] == usernm1:
                print("存在该用户信息")
                return login()
        else:
            passwd1=input("username1:")
            f1.writ("\n")
            f1.writ("usernm1")
            f1.write("\t")
            f1.write("passwd1")
            global user_status
            user_status={"usrname":usernm1,"password":passwd1}

@wrapper
def article():
     print("article")

@wrapper
def diary():
    print("diary")

@wrapper
def comment():
    print("comment")

@wrapper
def collection():
    print('欢迎来到收藏页')

@wrapper
def logout():
    print("logout")
    global user_status
    user_status={"usrename":None,"status":False}

@wrapper
def exited():
    print("exit")
    global Flag
    Flag=False

def choice2():
    global user_status
    if user_status["status"]:
        print("请选择页面序号")
        for k,v in dic2.items():
            print(k,v)
        choice=input("请选择序号").strip()
        if choice.isdigit():
            choice=int(choice)
            if choice == 3:
                pass



















