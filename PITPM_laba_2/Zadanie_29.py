class User:
  def setName(self, name):
    self.name = name

  def getName(self):
    return self.name

class Employee(User):
  pass

employee = Employee()

employee.setName('Troi')

name = employee.getName()
print(name)