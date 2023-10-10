class Employee:
  __name = None

  def __init__(self, name):
    self.__name = name

'False'
emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 == emp2)

'True'
emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 == emp1)

'False'
emp1 = Employee('john')
emp2 = Employee('john')

print(emp1 == emp2)

'False'
emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 != emp1)

'True'
emp1 = Employee('john')
emp2 = emp1

print(emp1 == emp2)

'True'
emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 != emp2)

'True'
emp1 = Employee('john')
emp2 = emp1
emp2.name = 'eric'

print(emp1 == emp2)