class User:
    def setName(self, name):
        if self.notEmpty(name):
            self.name = name

    def getName(self):
        return self.notEmpty(self.name)

    def notEmpty(self, stri):
        return len(stri) > 0

class Employee(User):
    def setSurn(self, surname):
        if self.notEmpty(surname):
            self.surname = surname

    def getSurn(self):
        return self.notEmpty(self.surname)

employee = Employee()

employee.setName('Gven')
employee.setSurn('Mach')

print(employee.getName(), employee.getSurn())