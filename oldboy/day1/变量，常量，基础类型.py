''''''

'''变量'''
# python将一些中间结果暂存到内存中，以便后续程序调用
    # 变量规则：
        # 由数字，字母，下划线任意组合
        # 不能以数字开头,不能包含空格
        # 不能是关键字和函数名【 and, as, in, is, for , try, break, class, continue, def, else, execpt, exec, finally, from, global, if, import, lambda, not, or, pass, print, raise, return, while, with】
    # 具有描述性
        # name = 'wzs'
        # 不能使用中文，和拼音(low)
    # 建议使用：
    # 下划线:name_wzs =
    # 驼峰体: FisrtName =

    # 下列变量名不行
        # a_ @ 和
        # 1  # 有特殊字符
        # _
        # _
        # 空格是特殊字符



'''常量'''
    # 常量：python中为与其他语言一致，所设置
    # 其是固定不变：如身份证号码
    # 将变量全部大写（规范），常量一般放在文件的最上面




'''基础数据类型'''
# 数字：int
    # 整数
    # 浮点数
        # 1.不能表示无限不循环小数
        # 2.小数位的不准确，越是小数位长越不精准
        # 计算机一切由二进制表示，其表示小数位会不准确
    # 复数complex ：1 + 2j  3+4j 【x平方=-1】
        # 1.复数是不能用来比较大小的
        # 2.共轭复数 ： 1 + 2j  / 1 - 2j


# 布尔值：：bool
    # True，False
    # 判断真假



# 字符串：str
    # 存储少量数据类型
    # python中：凡是用单/双引号引起来的数据就是字符串。
    # str = 'wuzhisheng   吴志盛'
    # str1 = "wuzhisheng   吴志盛"
    # wu='''   '''

    # # """ """或'''  ''' 保留格式

    # 字符串可以用 + 或 *
    # + 将字符串进行拼接
    # first_name = "ada"
    # last_name = "lovelace"
    # full_name = first_name + " " + last_name

    # w = 'wu'
    # z = 'zhi'
    # # 加可以
    # print(w + z)
    #
    # print(w * 3)


# 各种运算符
    # + - * / ** %
    # >= <= == > <
    # and or not
    # in   not in
    # is /is not
    # l1 = [1,2,3]
    # l2 = [1,2,3]
    # l3 = l1
    # print(id(l1),id(l2),id(l3))
    # print(l1 == l2)
    # print(l1 is l2)
    # print(l1 is not l2)
    # print(l1 is l3)

name = input('请输入姓名：')
age = input('请输入年龄：')
print ('用户姓名是:'+ name + '\t年龄是:'+ age)

#在字符串中使用整数时,需要将整数用作字符串
#否则会报错
age = 23
message = "Happy " + str(age) + "rd Birthday!"