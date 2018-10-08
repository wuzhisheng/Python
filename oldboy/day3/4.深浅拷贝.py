# copy
# 如果对容器数据类型(列表 字典 元组) 进行浅copy
# 那么这个数据中第一层所有的内存地址都会被copy下来
# 效果 ： 如果直接对这个数据的第一层进行操作 ：增 删 改 查 那么 两个数据是不会互相冲突的，变化一致
# 但是如果对数据类型内部的可变数据类型的元素进行修改，两个数据共享这个修改的成果
import copy  # copy是一个别人人好的python代码，你直接用就行了
lst = [1,2,3,4]
new_lst = copy.copy(lst)
print(new_lst,lst)
print(id(new_lst),id(lst))
new_lst.append({'key','value'})
print(new_lst,lst)

dic = {'key':'v'}
lst = [1,2,3,4,dic]
new = copy.copy(lst)  # 浅copy
print(new,lst)
dic['key'] = 'vvv'  #
print(new,lst)


# 深copy ： deepcopy
#完全copy一份，包括内存空间id,两者完全隔离
# 1.发生了深copy的两个数据之间没有任何关系了
# 2.占用内存
dic = {'key':'v'}
lst = [1,2,3,4,dic]
new = copy.deepcopy(lst)
dic['key'] = 'vvv'
lst[4]['key'] = 'nnnnn'
print(new,lst)

'''
设计数据类型的时候：
    不要做太多层的嵌套
能用浅copy的时候不要用深copy
尽量不要用copy
在python当中 所有的值传递 都是内存地址
'''




