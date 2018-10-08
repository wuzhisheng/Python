# set集合
    # 去重
    # 关系运算


# 集合
    # {'k':'v'} 字典   有序
    # {'k1','k2'}集合  无序,去重,只能使用可hash的数据类型

#去重
    #没有set
l = [1,1,1,1,2,3]
print(l)
new_l = []
for i in l:
    if i not in new_l:
        new_l.append(i)
print(new_l)

    #用set
se = {1,1,1,1,2,3}
print(se)

l = [1,1,1,1,2,3,4,5,6,6,'aaa','bbbb']
print(set(l))
print(list(set(l)))

se = {(1,2,3),(1,2,3),12,'abc'}
print(se)

# 关系运算 ： 求并集 交集 差集（补集） 对称差集
python = {'tangmeng','yangshixiong','zhuosenbin'}
linux = {'zhangsan','lisi','zhuosenbin'}
print(python|linux)  # 并集
print(python&linux)  # 交集
print(python-linux)  # 差集 只学python
print(python^linux)  # 对称差级


# 集合的要求：
    # 所有的元素必须可hash
    # 不能重复
    # 无序
# 能做的事情
    # 去重
    # 关系运算 ：求并集（全集）|  交集&  差集（补集）-  对称差集^
    # 增删改查 - 非重点








