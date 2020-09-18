class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometer = 0  # 里程
        self.oil_tank = 300  # 油箱

    def get_car_description(self):
        description = self.brand.upper() + ' ' + self.model.title() + ' ' + str(self.year)
        print(description)

    def get_kilometer(self):
        return self.kilometer

    def update_kilometer(self, kilometer):
        if kilometer > self.kilometer:
            self.kilometer = kilometer
        else:
            print("error, the new kilometer smaller than current!")

    def increase_kilometer(self, kilometer):
        self.kilometer += kilometer

    def fill_oil_tank(self):
        print("The car oil tank's size is ", self.oil_tank)


# 继承
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        """初始化并继承父类的属性"""
        super().__init__(brand, model, year)
        """定义子类自己的属性：电池"""
        """Battery 实例用作ElectricCar 类的一个属性"""
        """创建一个新的Battery实例 ， 并将该实例存储在属性self.battery_size 中。"""
        self.battery_size = Battery(battery_size)

    """定义子类自己的方法"""
    def get_battery_size(self):

        return self.battery_size

    """重写父类的方法"""
    def fill_oil_tank(self):
        print("The electric car no need oil tank")


class Battery():
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def description_battery_size(self):
        print("The car's battery is %d" % self.battery_size, '-KWH.')


# super() 是一个特殊函数， 帮助Python将父类和子类关联起来。
# 调用父类的方法__init__() ， 让子类 实例包含父类的所有属性。
# 父类也称为超类 （superclass） ， 名称super因此而得名
my_tesla = ElectricCar('tesla', 'model_s', 2020, 3000)
my_tesla.get_car_description()
my_tesla.fill_oil_tank()

# 将实例用作属性
my_tesla.battery_size.description_battery_size()
