#  1. 访问列表
lists01 = ['zhangsan', 'lisi', 'wangwu']
print(lists01)  # 打印全部
#  下标访问
print(lists01[0])
print(lists01[-1])
list2 = ['zhangsan', 'lisi', ['wangwu', 'wangliu']]
print(list2[2][1])

#  2. 修改列表
#  先指定位置, 再修改
lists01[1] = 'lili'
print(lists01)

#  添加元素
#   append() 在末尾添加元素
lists01.append('jack')
print(lists01)  # ['zhangsan', 'lili', 'wangwu', 'jack']

#  insert() 添加指定位置元素
lists01.insert(3, 'tony')
print(lists01)  # ['zhangsan', 'lili', 'wangwu', 'tony', 'jack']

#  3. 删除元素
#  pop(), 默认删除最后一个元素,并返回删除的元素,可以再使用
print(lists01.pop())
print(lists01)
# 删除指定位置元素
print(lists01.pop(0))
print(lists01)

#  del 删除之后无法再访问
del lists01[0]  # 删除第一个
print(lists01)

#  del list1  #  删除整个列表，从内存中删除，不能再访问list1
#  print(list1)

# 如果要从列表中删除一个元素， 且不再以任何方式使用它， 就使用del 语句； 、
# 如果你要在删除元素后还能继续使用它， 就使用方法pop() 。

#  remove  删除指定值的元素
#  remove() 只删除第一个指定的值。
#  如果要删除的值可能在列表中出现多次， 就需要使用循环来判断是否删除了所有这样的值。
#  list1.remove('tdonddy') #  不存在则报错
print(lists01)

#  3. 组织列表
# 3.1 sort, 永久修改顺序，按字母小至大顺序排序
lists01 = ['aa', 'cc', 'bb', 'ab', 'bc']
lists01.sort()
print(lists01)
# 按字母由大致小排序
lists01.sort(reverse=True)
print(lists01)

# 3.2 sorted()  临时排序
lists01 = ['aa', 'cc', 'bb', 'ab', 'bc']
print(sorted(lists01))
print(lists01)

print(sorted(lists01, reverse=True))
print(lists01)

# 3.3 revers() 列表逆置,不做排序
lists01.reverse()
print(lists01)

# 3.4 len() 确定列表长度
print(len(lists01))

# 3.5 避免索引错误
# print(list1[6])

# 4 创建数值列表
# 4.1 range() 生成数字
for num in range(1, 6):
    print(num)  # 打印数值1,2,3,4,5

# 4.2 使用range生成数字列表
nums = list(range(1, 6))
print(nums)

# 制定步长
nums = list(range(1, 10, 2))
print(nums)

squares = []
for num in nums:
    squares.append(num ** 2)
print(squares)

# 4.3 数字列表的统计计算
digits = [1, 2, 3, 4, 5, 6, 7]
print("min: ", min(digits))
print("max: ", max(digits))
print("sum: ", sum(digits))

# 4.4 列表解析, 优化代码
# for 循环为for value in range(1,11), 它将值1~10提供给表达式value**2
squares = [num ** 2 for num in range(1, 11)]
print(squares)

# 4.5 切片, 处理列表的部分元素
lists01 = ['aa', 'bb', 'cc', 'EM算法']
print(lists01[1:3])  # ['bb', 'cc']
print(lists01[:3])  # ['aa', 'bb', 'cc']
print(lists01[1:])  # ['bb', 'cc', 'EM算法']
# 负数索引返回离列表末尾相应距离的元素
print(lists01[-3:])  # ['bb', 'cc', 'EM算法']

# 切片遍历
print("只遍历前三个: ")
for list01 in lists01[0:3]:
    print(list01)

# 4.6 复制列表
lists01 = ['aa', 'bb', 'cc', 'EM算法']

# 使用切片复制
lists02 = lists01[:]
# 不使用切片复制, 相当于别名， 一份内存
# lists02 = lists01

print(lists01)
print(lists02)

lists01.append("01")
lists02.append("02")
lists01[0] = 'xx'
print(lists01)
print(lists02)
