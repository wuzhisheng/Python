#编码初始
''''''
'''
ascii: 只含英文，字母和数字
a: 01100001 8位表示1字节（256）

Unicode: 万国码
初始版：
a: 01100001 01100001  16位表示两字节 （65535）
更新版：
a:01100001 01100001 01100001 01100001 32位表示4字节
占内存

utf-8:最少8位，表示一个字符
a: 01100001 1字节
欧洲：01100001 01100001  2字节
亚洲：01100001 01100001 01100001   3字节
“老男孩boy” ：有6个字符，9个字节

gdk:国标（只含中文和英文）

中国gdk
英文：1个字节
中文：2个字节

日本gdk
英文：1个字节
日文：2个字节

“老alex”:五个字符
ascii:报错
unicode:20  
utf-8:7
gdk:6

8bit=1 bytes
1024bytes=1kb
1024kb=1MB
1024GB=1TB

字符串：存储少量的数据
'''
'''
int  str
int --> str : str(int)
str --> int: int(str)字符串全部由数字组成

int boot
int --> bool:非零即True
bool --> int:True 1  False 0

bool str:
	str --> bool：‘无数据‘ False,非空即True
	bool --> str: str(True)
'''
'''
[头：尾：隔和方向]
'''
s='吴志盛看海贼王路'
s4=s[:2] #吴志
print(s4)
s5=s[2:4] #盛看
print (s5)
s6=s[:5:3] #吴看
print (s6)
s7=s[-1:-4:-1] #路王贼
print (s7)
s8=s[-1:4:-1] # 路王贼
print (s8)
s9=s[:] #显示全部
print (s9)
print(s[:])  #显示全部
