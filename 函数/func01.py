# 1. 无参
def hello():
    """print hello"""
    print("hello")


print("ready: ")
hello()


# 2. 传参
def hello(hello_world):
    """print hello world"""
    print(hello_world)


hello('hello world')


# 3. 关键字实参, 实参和形参值关联， 不用考虑顺序
def hello__world(hello, world):
    print(hello + "__" + world)


hello__world(hello='hello', world='world')


# 4. 默认值, 从左到右 即先列出没有默认值的形参， 再列出有默认值的实参。
def hello__xx(x_x, hell='Hello'):
    print(hell + x_x)


hello__xx('Python')


# 5. 返回值
def get_format_name(firstname, lastname):
    fullname = firstname + " " + lastname
    return fullname.title()


name = get_format_name('zhang', 'san')
print(name)
print(get_format_name('zhang', 'san'))


# 6. 返回字典
def get_person(firstname, lastname):
    person = {'firstname': firstname, 'lastname': lastname}
    return person


person = get_person('zhang', 'san')
print(person)


# 7. 传递列表
def hello_xx(xx_list):
    for x in xx_list:
        print("hello", " ", x)


list01 = ['Python', 'Java', 'C']
hello_xx(list01)

# 7.1 在函数中修改列表， 永久性修改
print()


def hello_xx2(xx_list):
    i = 0
    for x in xx_list:
        if x == "C":
            xx_list[i] = x = 'C++'

        print("hello", " ", x)
        i += 1


print(list01)  # ['Python', 'Java', 'C']
hello_xx2(list01)
print(list01)  # ['Python', 'Java', 'C++']

# 7.2 禁止修改列表， 切片表示法[:] 创建列表的副本
print()
list01 = ['Python', 'Java', 'C']


def hello_xx3(xx_list):
    i = 0
    for x in xx_list:
        if x == "C":
            xx_list[i] = x = 'C++'

        print("hello", " ", x)
        i += 1


print(list01)  # ['Python', 'Java', 'C']
hello_xx2(list01[:])
print(list01)  # ['Python', 'Java', 'C']

# 8. 传递任意数量的参数
print("传递任意数量的参数")


def hello_xx4(*points):
    for p in points:
        print("hello", " ", p)


hello_xx4('Python', 'Java', 'C')


# 注： 如果还有别的参数， 那么这些参数只能写在 *points的前面
# 例： def hello_xx4(A, B, *points):
# 前两个参数分别由A，B接收。 剩下的全部由points接收


# 9. 使用任意数量的关键字实参
# 预先不知道传递给函数的会是什么样的信息。
# 在这种情况下， 可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
# 一个这样的示例是创建用户简介： 你知道你将收到有关用户的信息， 但不确定会是什么样的信息。
# 在下面的示例中， def build_profile(first, last, **user_info): 接受名和姓， 同时还接受任意数量的关键字实参：
# 形参**user_info 创建一个名为user_info 的空字典， 并将收到的所有名称—值对都封装到这个字典中
# 两个键—值对 age=18, sex='man'
def build_profile(first, last, **user_info):
    """" 创建字典， 包含用户的信息"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for k, v in user_info.items():
        profile[k] = v

    return profile


user_profile = build_profile('li', 'si', age=18, sex='man')
print(user_profile)

# 10. 将函数存储在模块（独立文件， import  文件名）中
import func02

func02.student_course('zhangsan', 'Python', 'Java')
func02.student_course('lisi', 'C++', 'Java')

# 10.1 导入特定的函数
# 10.13 导入模块中的所有函数 from func02 import  *
from func03 import func03_1, func03_2
func03_1()
func03_2()

# 10.2 使用as给模块/函数起别名
from func03 import func03_3 as f03_3
f03_3()

