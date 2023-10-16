class User:
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

class Employee(User):
    def incName(self):
        if (len(self._name) > 0):
            self._name = self._name

employee = Employee()

employee.setName('Skrydg')

print(employee.getName())