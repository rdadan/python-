# open('filename'), 返回文件对象 file_object
# 关键字with 在不再需要访问文件后自动将其关闭， 不必手动调用close()
# read() 到达文件末尾时返回一个空字符串，
with open('tt.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# 1. 逐行读取
print("\nread on line\n")
filename = 'tt.txt'
with open('tt.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())

# 2. 创建包含文件各行内容的列表
print("\nread on line save in list\n")

with open('tt.txt') as file_obj02:
    """从文件中读取每一行， 并将其存储在一个列表中"""
    lines = file_obj02.readlines()

# with 之外依然可以使用 lines
for line in lines:
    print(line.rstrip())


# 3。 使用文件内容
print("\nread file and use contents\n")
str03 = ''
# with open('tt.txt') as file_obj03:
# lines = file_obj02.readlines()
for line in lines:
    str03 += line.title().rstrip() + ' '

print(str03)


