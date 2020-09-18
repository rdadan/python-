import sys
sys.path.append("D:\开发项目\python_project\python基础语法\类")


#from creat_class.createclass import Car
#from creat_class.createclass import Car, Dog
#from creat_class.createclass import *

"""


car1 = Car("audi", "a6", 2020)
car1.get_car_descrition()
print("----")

dog1 = Dog("xiaoHei", 6)
dog1.sit_down()

"""

# 导入整个模块
import creat_class.createclass as cc
print("----")
car1 = cc.Car("audi", "a6", 2020)
car1.get_car_descrition()
dog1 = cc.Dog("xiaoHei", 6)
dog1.sit_down()
print("----")