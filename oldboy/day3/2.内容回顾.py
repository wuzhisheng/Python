# 基础数据类型

    # 数字类型 ：+ - * / % ** //
        # 整数
        # 浮点数
            # 1.不能表示无限不循环小数
            # 2.小数位的不准确，越是小数位长越不精准
            #计算机一切由二进制表示，其表示小数位会不准确
        # 复数complex ：1 + 2j  3+4j 【x平方=-1】
            # 1.复数是不能用来比较大小的
            # 2.共轭复数 ： 1 + 2j  / 1 - 2j

#不可/可变：看添加元素时，id(内存空间)是否改变。

    # 序列类型
        # 字符串 ： 不可变
            # + *
            # index 切片
            # replace split strip startswith join

        # 列表
            # 增删改查 ：append pop 改和查都是用索引
        # 元组 ： 不可变的
    # 散列类型
        # 字典 ：
            # key;value
            # key必须可hash（不可变数据类型），不能重复
            # 3.6以后的版本字典有序了
# 深浅copy，集合
# 流程控制 ：
    # 条件
# a = 100
# if a>90 :
#     pass
# elif a>80:
#     pass
# elif a>70:
#     pass
# else:
#     pass
    # 循环
        # while循环 ：不知道具体要循环多少次
            # 死循环 无限循环
            # 满足条件才推出
        # for循环 ： 知道要循环的次数
            # for i in range(100)
            # for i in list/tuple/dict/str
        # break
        # continue
        # else ：当循环没有被break，正常结束的时候 执行else中的代码
# 格式化输出
    # ‘%s’ ‘%d’ ‘%r’
# print('(%s)-（%r）'%('abc','abc'))
# print('%r'%'1')
# print('%r'%1)

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

# 编码
    # ascii
    # unicode 存的时候有很多浪费
    # gbk
    # utf-8 存的时候比较灵活