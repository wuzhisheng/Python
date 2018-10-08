# 文件操作
    # 文件的操作流程
        # 把文件打开
        # 选择你要做的操作 ： 读/写
        # 把文件关上

# 文件的读操作
#f 文件操作符/文件句柄（handler）
#read()
f = open(r'E:\志盛\python\python练习题\oldboy\day3\staff_info',encoding='utf-8')
content = f.read(5)
# print([content])  #[] 可显示打印字符串类型
print(content)
f.close()

#readline
f = open(r'E:\志盛\python\python练习题\oldboy\day3\staff_info',encoding='utf-8')
content1 = f.readline()
content2 = f.readline()
content3 = f.readline()
content4 = f.readline()  #读空行，没显示东西。但不会报错
print(content1.strip(),content2.strip(),content3.strip())
print([content4])
f.close()

#for 遍历文件每行
f = open(r'E:\志盛\python\python练习题\oldboy\day3\staff_info',encoding='utf-8')
for line in f:
    print(line.strip())
f.close()

# 路径
    # 1.如果当前要执行的代码和文件在同一个目录下，那么可以直接使用文件名
    # 2.如果当前要执行的代码和文件不在同一个目录下，就需要指定绝对路径，r''中
    # 3.你的目录最好是全英文，只由数字字母下划线组成

# 中文的文件  encoding = 'utf-8'
    # windows里 默认编码 gbk
    # mac linux 默认编码utf-8

# 读
    # read() 读所有内容              # 很少用
    # read(n) 读五个字符
    # readline 按照行读 不知道结束   # 不常用
    # for line in f  # 用的比较多的方式

f = open(r'E:\志盛\python\python练习题\oldboy\day3\a.txt')
sum_count = 0
for line in f:
    line = line.strip()
    lst = line.split(' ')
    sum_count += int(lst[1])*int(lst[2])
print(sum_count)
f.close()

# 写
# 以w的模式打开一个文件：
    # 如果文件不存在 ： 创建这个文件
    # 如果文件存在：清空这个文件
# write : 直接把write的参数（字符串数据类型）写入文件里
# writelines : 接收一个由字符串组成的列表/元组，把每一项都按照顺序写入
# 中文 encoding='utf-8'

f.write('字符串数据类型的内容')
f = open('write_file',mode='w')   # 文件清空
f.write('sgdligywojdbsvLfweui11111')
f.write('sgdligywojdbsvLfweui22222')
f.close()

# 中文 encoding='utf-8'
f = open('write_file',mode='w',encoding='utf-8')
f.write('字符串数据类型的内容')
f.close()

# 换行
f = open('write_file',mode='w',encoding='utf-8')
f.write('第一行\n')
f.write('%s\n'%'第二行')
f.close()

# writlines
f = open('write_file',mode='w',encoding='utf-8')
f.writelines(['第一行\n','第二行\n'])
f.close()

# 追加写 a
f = open(r'E:\志盛\python\python练习题\oldboy\day3\write_file',mode='a',encoding='utf-8')
f.write('第三行')
f.close()

# 操作文件的模式
    # r  读
    # w  写
    # a  追写

# 可读可写 r+
#写在原来内容追加，但没有换行
#写write后再读是在第一个读，后面接着读
f = open('write_file',mode='r+',encoding='utf-8')
content = f.read(9)
print(content)
f.write('hello,world')
content2 = f.read(3)
print(content2)
f.close()


# seek/tell的时候 返回的值和参数都是以字节为单位的
# read的时候 单位 字符
f = open('write_file',mode='r+',encoding='utf-8')
content = f.read(9)
print(content,f.tell())  # 告诉我当前文件的光标所在的位置
f.seek(3)         # 移动光标到指定的位置
content = f.read(9)
print(content,f.tell())
f.close()


# 光标 -- 文件指针
f = open('write_file',mode='r+',encoding='utf-8')
content = f.read(9)
print(content)
f.seek(3)
f.write('你好')
content = f.read()
print(content)
f.close()

# 处理文件的格式不要边读边写
# 修改  不能这么写
f = open('write_file',mode='r+',encoding='utf-8')
f.seek(3)
f.write('再见吧')
print('再见吧'.encode('utf-8'))
f.close()

# 可写可读 w+
# 首先会被清空
# 写
# 已经写进去的东西 你可以读
# 你需要自己调整光标的位置 seek(0)

# 追加可读 a+

# 操作文件的模式
    # r  读  rb
    # w  写  wb
    # a  追写 ab
    # r+ 可读可写 需要我们自己调整文件指针 尽量少用  rb+
    # w+ 几乎不用
    # a+ 追写可读 需要我们自己调整文件指针 尽量少用
# 读 ：
    # read() 读所有内容              # 很少用
    # read(n)                        # 处理大文件的时候 常用
        # 如果以r的形式打开 表示读n个字符
        # 如果以rb的形式打开 表示读n个字节
    # readline 按照行读 不知道结束   # 不常用
    # for line in f  # 用的比较多的方式   # 处理文字类型文件非常常用
# 写：
    # write : 直接把write的参数（字符串数据类型）写入文件里
    # writelines : 接收一个由字符串组成的列表/元组，把每一项都按照顺序写入
# 操作文件指针，单位都是字节
    # seek
    # tell

# 如果要操作的是图片或者视频怎么办
# rb
# wb
'p1_bak.png'
p1 = open('p1.png','rb')
content = p1.read()
p1.close()

p2 = open('p1_bak.png','wb')
p2.write(content)
p2.close()

# 文件的上下文管理
p1 = open('p1.png','rb')
content = p1.read()
p1.close()

with open('p1.png','rb') as p1:
    content = p1.read()

# 文件的修改
import os
f1 = open('a.txt',mode='r',encoding='utf-8')
f2 = open('a.txt.bak',mode='w',encoding='utf-8')
for line in f1:
    if line.startswith('tesla'):
        line = line.replace('1000000','800000')
    f2.write(line)
f1.close()
f2.close()
os.remove('a.txt')   # 删除文件
os.rename('a.txt.bak','a.txt')  # 重命名文件


import os
with open('a.txt',mode='r') as f1,open('a.txt.bak', mode='w') as f2:
    for line in f1:
        if line.startswith('tesla'):
            line = line.replace('1000000','800000')
        f2.write(line)
os.remove('a.txt')
os.rename('a.txt.bak','a.txt')





