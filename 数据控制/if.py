# 1. 示例
lists01 = ['aa', 'bb', 'cc', 'EM算法']
str01 = 'bb'
for list01 in lists01:
    if str01 == list01:
        print("list01 == bb, ", list01.upper())
    else:
        print(list01.title())

# 2. and, or
age = 220
if 18 < age < 30:
    print(18 < age < 30)
else:
    print(18 < age < 30)

age1 = 20
age2 = 110
if (age1 > 15) and (age2 < 15):
    print("True")
else:
    print("False")

# 3. in, not in

if "aa" in lists01:
    print("True")
else:
    print("False")

# 4. bool 表达式
str01 = 'bbb'
print(str01 == 'bbb')

# 5. if语句
age = 101
if age < 8:
    print("age < 8")
elif age < 18:
    print("age < 18")
else:
    print(age)

lists01 = []
if lists01:
    print("not null")
else:
    print("null")
lists02 = ['ww']
if not lists02:
    print("null")
else:
    print("not null")

lists01 = ['aa', 'bb', 'cc', 'EM算法']
lists02 = ['aa', 'cc']

for lt in lists01:
    if lt in lists02:
        print("%s in lists02" % lt)
    else:
        print("%s not in lists02" % lt)
