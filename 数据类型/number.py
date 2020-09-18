# 1. int
a = 1
# type() 查看数据类型的函数
print(type(a))

# 2. bool
a = True
print(type(a))

# 3.string
# 带上引号的都是字符串
# 单引号 ‘’
# 双引号 “”， 如果单引号本身是字符的话，就要用双引号
# 如果字符串内部包含 ‘或者 “作为普通字符，可用转义字符 \ 来标识

a = "刘德华"
b = '黎明'
c = '1'
print(type(a))
print(type(b))
print(type(c))  # <class 'str'>

str1 = '"nihao"'  # 双引号成为字符串本身 "nihao"
str2 = "'nihao'"  # 单引号成为字符串本身 'nihao'
print(str1)
print(str2)

# \ 转义字符
str1 = 'aaa\'bbb'  # aaa'bbb
print(str1)

# 截取字符串 变量[开始下标：结束下标],
str0 = 'abcdefg'
print(str0[0])  # a
print(str0[0:3])  # abc
print(str0[1:])  # bcdefg, 到最后。
print(str0[:2])  # ab。包左不包右

print(str0[-1])  # g   反过来，最后一位
print(str0[-2])  # f   倒数第二位
print(str0[1:-1:2])  # bdf 步长2位,即跨一位

print(str0[::-1])  # gfedcba
print(str0[5:1:-2])  # fd

# 只要是空都是False
str0 = ''
print(bool(str0))  # 空字符串，返回False

str0 = []
print(bool(str0))  # 空列表，返回False

str0 = ()
print(bool(str0))  # 空元组，返回False


str0 = {}
print(bool(str0))  # 空字典，返回False

num = 0
print(bool(num))  # 0，bool返回False

#print(str[100])  #  空 IndexError: string index out of range



