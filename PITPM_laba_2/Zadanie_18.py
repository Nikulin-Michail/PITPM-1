class Employee:
    __salary = None
    __age = None

    def getSalary(self):
        return self.__salary + '$'

    def getAge(self):
        return self.__age

    def setSalary(self, salary):
        self.__salary = salary

    def setAge(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            raise Exception("age is incorrect!")

employee = Employee()

employee.setSalary('150')
employee.setAge(54)

print(employee.getSalary())
print(employee.getAge())