name = 'zhangsan'
age = 18
address = 'shanghai'

print('大家好, 我叫%s, 我今年%d岁, 我来自%s' % (name, age, address))

#  find, 查找到返回字符串的位置，找不到返回-1
#  index, 找到返回位置，找不到报错
str = 'i am a student'
print(str.find('ud'))
print(str.index('ud'))

#  count
print(str.count('a'))  # 从头到尾查找a的个数
print(str.count('a', 0, 3))  # 从位置1到3查找a的个数

#  replace
print(str.replace('a', 'A', 1))

#  split, 返回一个列表
print(str.split(' '))  # ['i', 'am', 'a', 'student']

# 修改单词大小写 title()
str0 = 'heLlo, woRd!'
print(str0.title())
print(str0.lower())
print(str0.upper())

# 拼接字符串
str1 = 'hello'
str2 = 'world'
str3 = str1 + " - " + str2
print(str3)
print("Python, " + str0.title() + "!")

str4 = 'Python, ' + str0.title() + '!'
print(str4)

# \t制表符
print("aaaa没制表符")
print("\taaaa有制表符")

# \n换行符
print("Languages: \n\tPython\n\tC++\n\tC")

# 删除空白
# 删除末尾全部空白 rstrip()
str0 = 'Python  '
print(str0, len(str0))
str0 = str0.rstrip()
print(str0, len(str0))

# 删除开头全部空白
str0 = '  Python  '
print(str0, len(str0))
str0 = str0.lstrip()
print('lstrip: ', str0, len(str0))

# 删除两端全部空白
str0 = '  Python  '
str0 = str0.strip()
print('strip: ', str0, len(str0))
