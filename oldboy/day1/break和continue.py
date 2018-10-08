
#break 只要遇到break，就立马跳出循环体
while True:
    print ('wu')
    print('sheng')
    break
    print('zhi')

count=1
while count < 5:
    if count >= 3:
        break
    count=count+1
else:
    print('循环结束...')
print(6666)

#continue 立马跳回while开头重新开始
while True:
    print ('wu')
    print('sheng')
    continue
print('zhi')
