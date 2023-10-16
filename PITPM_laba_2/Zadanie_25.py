class User:
  def __init__(self, name):
    self.__name = name

  def getName(self):
    return self.__name


class EmployeesCollection:
  def __init__(self):
    self.__employees = []

  def add(self, employee):
    self.__employees.append(employee)

  def show(self):
    for employee in self.__employees:
      print(employee.getName())

  def calculateTotalSalary(self):
    total_salary = 0
    for employee in self.__employees:
      total_salary += employee.getSalary()
    return total_salary

  def calculateAverageSalary(self):
    total_salary = self.calculateTotalSalary()
    num_employees = len(self.__employees)
    if num_employees == 0:
      return 0
    else:
      return total_salary / num_employees


class Employee:
  def __init__(self, name, salary):
    self.__name = name
    self.__salary = salary

  def getName(self):
    return self.__name

  def getSalary(self):
    return self.__salary


ec = EmployeesCollection()
ec.add(Employee('John Doe', 50000))
ec.add(Employee('Jane Smith', 60000))
ec.add(Employee('Mike Johnson', 55000))

ec.show()

total_salary = ec.calculateTotalSalary()
print(total_salary)   # Суммарная зарплата

average_salary = ec.calculateAverageSalary()
print(average_salary)   # Средняя зарплата
