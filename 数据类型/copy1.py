import copy as cp

list1 = ['aa', 'bb', 'cc']

# 1. 直接赋值
list2 = list1
print(list1)

list1[0] = 'aa'
print(id(list1))  # 地址相同
print(id(list2))

print("list1: ", list1)
print("list2: ", list2)

# 2. 切片操作
a = [1, 2, 3]
b = [11, 22, 33]
c = [111, 222, 333]

list01 = [a, b, c]
print(id(list01))

list02 = list01[:]
print("list01: ", list01)
print("list02: ", list02)

# 查看地址  地址不相同
print("list01: ", id(list01))  # 3068104461128
print("list02: ", id(list02))  # 3068104561096

a[0] = 'a'
# 值都被修改
print("list01: ", list01)  # [['a', 2, 3], [11, 22, 33], [111, 222, 333]]
print("list02: ", list02)  # [['a', 2, 3], [11, 22, 33], [111, 222, 333]]

# 3. 深拷贝
import copy as cp

list02 = cp.deepcopy(list01)
a[0] = 'b'
#  只有list01值被修改
print("deepcopy list01: ", list01)  # [['b', 2, 3], [11, 22, 33], [111, 222, 333]]
print("deepcopy list02: ", list02)  # [['a', 2, 3], [11, 22, 33], [111, 222, 333]]
