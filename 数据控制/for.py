# 1 for循环遍历列表
lists01 = ['aa', 'bb', 'cc', 'EM算法']
num = 0
for list01 in lists01:
    num += 1
    print(list01.title() + " in for" + " 这是第%d个\n" % num)

print("循环结束，一共循环%d次" % num)
