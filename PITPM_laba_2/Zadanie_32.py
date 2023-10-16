class User:
    def setAge(self, age):
        if (age >= 0):
            self.age = age
        else:
            raise Exception('need age more 0')

    def getAge(self):
        return self.age

class Employee(User):
    def setAge(self, age):
        if (age <= 120):
            super().setAge(age)
        else:
            raise Exception('need age less 120')

employee = Employee()

employee.setAge(25)

print(employee.getAge())