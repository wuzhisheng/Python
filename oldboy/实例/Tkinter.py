#=======================1
'''
Tkinter是python的标准GUI库，其是建立在Tk技术上
其移植性和灵活性高
'''
import tkinter as tk
#创建一个主窗口，用于容纳整个GUI程序
root=tk.Tk()
#设置主窗口对象的标题栏
root.title("FishC Demo")
# 添加一个Label组件，Label组件是GUI程序中最常用的组件之一
# Label组件可以显示文本，图标或图片
# 在这里我们让他显示指定文本
theLabel=tk.Label(root,text="my seconds windons")
#调用Label组件的pack()方法，用于自动调节组件自身尺寸
theLabel.pack()
#只有执行这条才会显示窗口，否者不会显示
root.mainloop()


#=====================2
'''
===1
frame.pack(side=tk.LEFT)左对齐
pack（）可设side=LEFT/RIGHT/TOP/TOTTOM
默认side=tk.TOP
#==== 2
frame.pack(side=tk.LEFT,padx=10,pady=10)
设置偏移位置
padx:10
pady:10
#=====3
设置背景颜色
bg ="black"
'''

import tkinter as tk
class App:
    def __init__(self,root):
        #创建一个框架，在其添加一个Botton按钮组件
        #框架:用于复杂的布局中起到将组件分组的作用
        frame=tk.Frame(root)
        frame.pack(side=tk.LEFT,padx=10,pady=10)
        #创建一个按钮组件，fg是foreground缩写：设置前景色i
        self.hi_there= tk.Button(frame, text="打招呼",bg ="red", fg ="yellow", command = self.say_hi)
        self.hi_there.pack(side=tk.LEFT)
    def say_hi(self):
        print("Hi world！")

#创建一个toplevel的根窗口，并把它作为参数实例化app对象
root=tk.Tk()
app=App(root)
#开始主事件循环
root.mainloop()

'''Label组件
在界面上输出描述的标签
'''
from tkinter import *
#导入tkinter模块的所有内容
root=Tk()
# 创建一个文本Label对象
textLabel=Label(root,\
text="该影片为动漫《海贼王》",justify=LEFT,padx=10)
textLabel.pack(side=LEFT)
#创建一个图像Label对象
#用photoimage实例化一个图片对象
photo=PhotoImage(file="1.png")
imgLabel=Label(root,image=photo)
imgLabel.pack(side=RIGHT)
mainloop()
'''
textLabel=Label(root,\
text="该影片为动漫《海贼王》",justify=LEFT,padx=10)
'''



'''
将图片作为背景
文字显示在图片上面
'''
from tkinter import *
root=Tk()
photo=PhotoImage(file="p1.png")
theLabel=Label(root,text="学Python\n到Fshit",
               justify=LEFT,
               image=photo,
               compound=CENTER,
               font=('华康少女字体',20),
               fg="red"
               )
theLabel.pack()
mainloop()


''''''
'''Button组件
实现一个按钮
其可接受用户
'''
from tkinter import *
def callback():
    var.set("吹吧你，我才不信呢")

#创建一个主窗口，用于容纳整个GUI程序
root =Tk()
framel=Frame(root)
frame2=Frame(root)
#创建一个文本Label对象
var=StringVar()
var.set("您下载动漫《海贼王》")
textLabel=Label(framel,
                textvariable=var,
                #按钮被单击后Label文本发生改变。想要文本发生改变，
                #需设置textvariable选项为Tkinter变量
                justify=LEFT)
#调用Label组件的pack()方法，用于自动调节组件自身尺寸
textLabel.pack(side=LEFT)
#创建一个图像Label对象
#用photoimage实例化一个图片对象
#调用Label组件的pack()方法，用于自动调节组件自身尺寸
photo=PhotoImage(file="1.png")
imgLabel=Label(framel,image=photo)
imgLabel.pack(side=RIGHT)
#加一个按钮
#command选项指定一个函数或方法，当用户单击按钮的时候，Tkinter
theButton=Button(frame2,text="动漫迷",command=callback)
#会自动调用这个函数或方法
theButton.pack()
#framel.pack定义上下排版间隔
framel.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)
mainloop()


'''Checkbutton组件 
多选按钮
'''
#====================
from tkinter import *
#创建一个主窗口，用于容纳整个GUI程序
root=Tk()
#需要一个Tkinter变量，用于表示该按钮是否被选中
v=IntVar()
c=Checkbutton(root,text="测试一下",variable=v)
c.pack(anchor=W)#指定显示位置设置N,NE,EE,SE,S,SW,W,NW
#如果选项被选中，那么变量v被赋值为1，否则为0
#可以用个Label标签动态给大家展示
# 添加一个Label组件，Label组件是GUI程序中最常用的组件之一
# Label组件可以显示文本，图标或图片
# 在这里我们让他显示指定文本
l=Label(root,textvariable=v)
#调用Label组件的pack()方法，用于自动调节组件自身尺寸
l.pack()
mainloop()

###???
from tkinter import *
root=Tk()
nv=["索隆","路飞","香吉士","哈"]
v=IntVar()
v.set(-1)
for girl in nv:
    b= Checkbutton(root,text=girl,variable=v)
    b.pack()
mainloop()



'''Radiobutton组件
实现单选，即同组Radiobutton只能共享一个variable选项，且value值不同
'''
from tkinter import *
root=Tk()
v=IntVar()
Radiobutton(root,text="One",variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="Two",variable=v,value=2).pack(anchor=W)
Radiobutton(root,text="There",variable=v,value=3).pack(anchor=W)
mainloop()


from tkinter import *
root=Tk()
LANGS=[
    ("python",1),
    ("perl",2),
    ("Ruby",3),
    ("Lua",4)
]
v=IntVar()
v.set(1)
for lang,num in LANGS:
    #indicatoron=False添加这个将圆圈设置为按钮形式
    b=Radiobutton(root,text=lang,variable=v,value=num)
    b.pack(anchor=W)
    #b = Radiobutton(root, text=lang, variable=v, value=num,indicatoron=False)
    # b.pack(fill=X)
mainloop()

'''LabelFrame组件
是Frame框架升级版
其使Checkbutton，Radiobutton变得简单
'''
from tkinter import *
root=Tk()
group=LabelFrame(root,text="脚本语言是：",padx=5,pady=5)
group.pack(padx=10,pady=10)
LANGE=[
    ("python",1),
    ("perl",2),
    ("Ruby",3)]
v=IntVar()
v.set(1)
for lange,num in LANGE:
    b=Radiobutton(group,text=lange,variable=v,value=num)
    b.pack(anchor=W)
mainloop()



'''Entry组件
输入框
'''
from tkinter import *
root=Tk()
e=Entry(root)
e.pack(padx=20,pady=20)
e.delete(0,END) #删除
e.insert(0,"默认文本....") #添加
mainloop()



from tkinter import *
#创建一个主窗口，用于容纳整个GUI程序
root=Tk()
#Tkinter提供三种布局组件：pack(),gird(),place()
#grid()用表格的形式来管理组件的位置
#row代表 行,column代表 列
#例如：row=1,column=2：第二行第三列（0表示第一行）
Label(root,text="作品:").grid(row=0)
Label(root,text="作者").grid(row=1)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("作品:《%s》" % e1.get())
    print("作者:%s" % e2.get())
    e1.delete(0,END)
    e2.delete(0, END)

#如果表格大于组件，则使用sticky选项来设置组件位置
#可用N,E,S,W及NE,SE,SW,NW来表示方位
Button(root,text="获取信息",width=0,command=show)\
    .grid(row=3,column=0,sticky=W,padx=10,pady=5)

Button(root,text="退出",width=0,command=root.quit)\
    .grid(row=3,column=1,sticky=E,padx=10,pady=5)
mainloop()



from tkinter import *
#创建一个主窗口，用于容纳整个GUI程序
root=Tk()
#Tkinter提供三种布局组件：pack(),gird(),place()
#grid()用表格的形式来管理组件的位置
#row代表 行,column代表 列
#例如：row=1,column=2：第二行第三列（0表示第一行）
Label(root,text="账号:").grid(row=0)
Label(root,text="密码").grid(row=1)
v1=StringVar() #输入框内容
v2=StringVar()
#星号(*)代替用户输入的内容
#Entry 可输入内容
e1=Entry(root,textvariable=v1)
e2=Entry(root,textvariable=v2,show="*")
e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("账号:《%s》" % e1.get())
    print("密码:%s" % e2.get())
    e1.delete(0,END)
    e2.delete(0, END)

#如果表格大于组件，则使用sticky选项来设置组件位置
#可用N,E,S,W及NE,SE,SW,NW来表示方位
Button(root,text="登录",width=0,command=show)\
    .grid(row=3,column=0,sticky=W,padx=10,pady=5)

Button(root,text="退出",width=0,command=root.quit)\
    .grid(row=3,column=1,sticky=E,padx=10,pady=5)
mainloop()


'''
Entry组件，除输入框外还支持验证输入内容的合法性
其功能需要
validate,validatecommand,invalidcommand

validate该选项设值
focus:Entry组件获得或失去焦点的时候验证
focusin:Entry组件获得焦点的时候验证
focusout:Entry组件失去焦点的时候验证
key:输入框被编辑的时候验证
all：以上任意情况时候验证
none：关闭验证功能（默认）
'''
from tkinter import *
root=Tk()
def test1():
    if e1.get() == "wzs":
        print("正确")
        return True
    else:
        print("错误")
        e1.delete(0,END)
        return False

def test2():
    print('我被调用了...')
    return True

v=StringVar()
#validatecommand 指定一个验证函数（只能返回True和False）
e1=Entry(root,textvariable=v,validate="focusout",validatecommand=test1)
e2=Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()
#第一个输入框中输入内容，通过Tab键将焦点转移到第二个输入框时，验证功能被触发




from tkinter import *
root=Tk()
v=StringVar()
def test1(content,reason,name):
    if content == "wzs":
        print("正确")
        print(content,reason,name)
        return True
    else:
        print("错误")
        print(content, reason, name)
        return False

testCMD=root.register(test1)
e1=Entry(root,textvariable=v,validate="focusout",validatecommand=(testCMD,'%P','%v','%W'))
e2=Entry(root)
e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)
mainloop()










