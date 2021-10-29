####### public , private, protected #######
class employee:
    def __init__(self, name, sal, age):
        self.name = name  # public attribute
        self.__salary = sal  # private attribute
        self._age = age  # protected attribute


e1 = employee("Bill", 10000, 27)
# print(e1.__salary)
print(e1._age)