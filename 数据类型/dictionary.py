# 键-值， 每一个键对应一个值
dict01 = {'A': 'a', 'B': 'b'}
print(dict01)  # {'A': 'a', 'B': 'b'}

# 1. 访问
print(dict01['A'])  # a
print(dict01['B'])  # b

# 2. 添加
dict01['C'] = 'c'
print(dict01)  # {'A': 'a', 'B': 'b', 'C': 'c'}

# 3. 修改
dict01['C'] = 'cc'
print(dict01['C'])

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# 4, 删除
# del 彻底删除，必须指定字典名和要删除的键
dict01 = {'A': 'a', 'B': 'b'}
print(dict01)
del dict01["A"]
print(dict01)

# 5. 遍历
# items() 返回一个键值对列表
user_0 = {'username': 'zhangsan', 'first_name': 'zhang', 'last_name': 'san'}
for k, v in user_0.items():
    print("key: ", k, ", value: ", v)
print('\n')

# 5.1 遍历所有的键
# keys(), 返回一个列表， 其中包含字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages.keys():
    print(name.title())

# 5.2 遍历所有的值
# values() ， 它返回一个值列表， 而不包含任何键
for name in favorite_languages.values():
    print(name.title())

# 5.3 遍历中对字典处理

# 1. 有序遍历 sorted(...)
print('\n')

for name in sorted(favorite_languages.values()):
    print(name.title())

# 2. 去除重复值 set(...)
print('\n')

for name in sorted(set(favorite_languages.values())):
    print(name.title())

# 6. 嵌套
# 6.1 字典放进列表
# 三个字典
computer_1 = {'brand': 'xiaomi', 'price': 4999}
computer_2 = {'brand': 'huawei', 'price': 6999}
computer_3 = {'brand': 'apple', 'price': 9999}
# 列表
goods = [computer_1, computer_2, computer_3]
print('\n')
for good in goods:
    print(good)

# 6.2 列表放进字典
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'c++'],
}
print('\n')
lan = ''
for name, languages in favorite_languages.items():
    for language in languages:
        lan += language.title() + ' '
    print(name.title() + "'s favorite languages are: ", lan)
    lan = ''

# 6.3 字典中存储字典
