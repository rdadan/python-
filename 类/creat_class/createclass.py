# 类创建
class Dog:
    """__init__() 创建对象时自动调用"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit_down(self):
        print(self.name.title(), " is sitting now!")

    def roll_over(self):
        print(self.name.title(), " is rolled over!")


# 创建对象
dog1 = Dog("xiaobai", 6)
# 访问成员
age = dog1.age
name = dog1.name
print(name, " is ", age, "years old!")
# 访问成员函数
dog1.sit_down()
dog1.roll_over()


# 2. 使用类和实例
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometer = 0

    def get_car_descrition(self):
        descriton = self.brand.upper() + ' ' + self.model.title() + ' ' + str(self.year)
        print(descriton, ", kilometers: ", str(car1.get_kilometer()))

    def get_kilometer(self):
        return self.kilometer

    def update_kilometer(self, kilometer):
        self.kilometer = kilometer

car1 = Car("bmw", "a3", 2020)
car1.get_car_descrition()

car1.kilometer = 100  # 法一
car1.update_kilometer(200)  # 法二
car1.get_car_descrition()
