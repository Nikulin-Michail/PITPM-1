class Employee:
  name = None
  salary = None

  def show_name(self):
    print(self.name)

  def show_salary(self):
    print(self.salary)

employee = Employee()

employee.name = 'Gleb'
employee.salary = '5000'

employee.show_name()  # выведет 'Gleb'
employee.show_salary()