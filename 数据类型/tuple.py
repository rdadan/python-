# 列表, 适用变化的数据集
# 元组, 用于创建不可修改的元素， 即不可改变的列表
ip_port = ("1.1.1.1", 8888)
# print(str(ip_port[0]))
# 访问
print(ip_port[0])
print(ip_port[1])
# 遍历
for ip_po in ip_port:
    print(ip_po)

# 修改, 会报错
# ip_port[1] = 6666

