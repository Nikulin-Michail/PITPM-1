class User:
    __name = None
    __surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(surname):
        self.__surname = surname

    def getSurn(self):
        return self.__surname

    def getFull(self):
        return self.__name + ' ' + self.__surname

class Employee(User):
    pass

employee = Employee()

employee.setName('Pem')
employee.setSurn('Smith')

name = employee.getName()
surn = employee.setSurn()

print(employee.getFull())
print(name, surn)