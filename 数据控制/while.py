# 1. while 循环
num = 5
while num > 0:
    #   print(num)
    num -= 1

# 2. 有用户输入决定循环结束
message = "please input something, or exit! \n"
print(message)
while message != 'exit':
    message = input()
    if message != 'exit':
        print("1 the message is : ", message, '\n')

# 3. 由标记确定是否结束循环
flag = True
message = ''
while flag:
    message = input()
    if message == 'exit':
        flag = False
    else:
        print("2 the message is : ", message, '\n')

# 4. break退出循环
message = ''
while True:
    message = input()
    if message == 'exit':
        break
    else:
        print("3 the message is : ", message, '\n')

# 5. continue
num = 10
while num > 0:
    if num % 2 == 0:
        print(num)
        num -= 1
    else:
        num -= 1
        continue

