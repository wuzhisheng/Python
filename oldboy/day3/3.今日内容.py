# 深浅copy
    # import copy
    # new = copy.copy(lst)       # 占用空间相对少，对于lst中的可变数据类型的修改，new也会跟着变
    # new2 = copy.deepcopy(lst)  # 占用的空间更多，完全分离了lst、new2两个数据
    # 在python中，所有的变量都是指向某个值得内存地址
    # 在程序设计中，尽量避免多层嵌套的copy动作
# 集合 set
    # 特点 ： 无序 去重 做运算 内部元素必须（可hash）不可变
    # 功能 ：
        # 去重
        # 运算 ： 并| 交& 补(差)- 对称差^
# 文件操作
    # 文件的操作模式 mode
        # 默认是r
        # w
        # a
        # rb wb ab 以字节的形式处理文件
        # r+ w+ a+ 不推荐你使用
    # 读写操作
        # 读
            # read()   ：占内存
            # read(n)  : 推荐
            # readline ： 不知道在哪儿停止
            # for line in f:  推荐
        # 写
            # write   ： 推荐
            # writelines(lst) : 不推荐
    # with open() as f:
        # 上下文管理 ： 简化操作，不需要手动关闭文件
    # 修改文件
        # 打开两个文件，边读 边修改 边写
        # import os
        # os.remove(原文件路径)
        # os.rename(修改之后的文件路径，原文件路径)
# 初识函数
    # 函数的定义
        # def 函数名(参数)：
            # 函数体
            # return 返回值
    # 函数的调用
        # 返回值变量 = 函数名(实际参数)
    # 参数
        # 形参
            # 位置参数
            # *args
            # 默认参数
            # **kwargs
        # 实参
            # 按照位置传参
            # 按照关键字传参数














