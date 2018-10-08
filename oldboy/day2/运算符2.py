#优先级：()>not>and>or
print (1 > 2 and 3 < 4 or 28 > 6 and 7 < 3 or 7 > 6) #true

'''
非0即true
0即False

int ----> bool
print(bool(100)) #True
print(bool(0)) #False
print (bool(-1)) #True
print (int(True)) #1
print (int(False)) #0
bool ---> int
print (int(True)) 1
print (int(False)) 0
'''

# x or y if x is True,return x
print (1 or 3 ) #1
print (0 or 3 ) #3
print (-4 or 3 ) #-4

# x and y if x is True,return y
print (3 and 6) #6
print(0 and 6 ) #0

print (1 or 4 and 7 ) #1
print (1 < 2 or 3 and 4 > 1) #ture