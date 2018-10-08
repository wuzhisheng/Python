
l = ['alex','wupeiqi','boss_jin','nezha','yuan']
# new_l = []
# for name in l:
#     new_l.append(name+'sb')
# print(new_l)

# new_l = [name+'sb' for name in l]
# print(new_l)

# 30以内所有能被3整除的数
# l = []
# for i in range(30):
#     if i % 3 == 0:
#         l.append(i)

# ret = [i for i in range(31) if i%3==0]
# print(ret)

# [1,-2,3,4,5,-6]  --> [1,2,3,4,5,6]
# l =[1,-2,3,4,5,-6]
# l = [abs(i) for i in l]
# print(l)

# 30以内所有能被3整除的数的平方
# ret = [i*i for i in range(30) if i%3 == 0]
# print(ret)

# 用if的时候 被循环的内容中不一定所有的值都在结果列表里

# 找到names中所有有两个e的名字
# names = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
#          ['Alice', 'Jill', 'Ana', 'Wendy', 'Jennifer', 'Sherry', 'Eva']]
#
# lst = [name for lst in names for name in lst if name.count('e') >=2]
# print(lst)

# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase}
# print(mcase_frequency)
# k = 'a'
# 'a' : 10 + 7 = 17
# k = 'b'
# 'b' : 34
# k = 'A'
# 'a' : 10 + 7 = 17
# k = 'Z'
# 'z' : 0 + 3 = 3


# mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
# ret = mcase.get('a',0)
# print(ret)