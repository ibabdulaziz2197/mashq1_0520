# 3
class Phone:
    def __init__(self, model, battery):
        self.model = model
        self.__battery = battery


    @property
    def battery(self):
        return self.__battery



    @battery.setter
    def battery(self, toza):
        self.__battery = toza



s = Phone('Iphone', 54000)

res = s.battery
print(res)

s.battery = 5
print(s.battery)


# 4
class Teacher:
    def __init__(self, fullname, salary):
        self.fullname = fullname
        self.__salary = salary


    @property
    def salary(self):
        return self.__salary



    @salary.setter
    def battery(self, toza):
        self.__salary = toza



s = Teacher('Iphone', 54000)

res = s.salary
print(res)

s.salary = 5
print(s.salary)

# 5
class Laptop:
    def __init__(self, brand, ram):
        self.brand = brand
        self.__ram = ram

    @property
    def ram(self):
        return self.__ram


    ram.setter
    def ram(self, toza):
        self.__ram = toza


s = Laptop('by', 15)

res = s.ram
print(res)

s.ram = 1
print(s.ram)
