
# 1. input 获取用户输入，存储在变量中
#message = input("请随意输入内容：")
#print("您输入的是: ", message)

# 2. 用int()获取整形输入
age = input("please input your age: ")
age = int(age)
if age >= 18:
    print("your age >= 18, and your age is: ", age)
else:
    print("your age < 18, and your age is: ", age)
