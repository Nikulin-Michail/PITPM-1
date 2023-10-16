class User:
    __name = '0'

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Employee(User):
    __name = '0'

    def __init__(self):
        __name = self.getName()

    def setName(self, name):
        if (len(name) > 0):
            self.__name = name

employee = Employee()

employee.setName('Max')

print(employee.getName())

