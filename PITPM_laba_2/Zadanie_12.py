class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_name(self):
        return self.name

    def show_salary(self):
        return self.salary

    def plus_salary(self):
        return (self.salary * 0.1) + self.salary

employee = Employee('Med', 1500)

print(employee.show_name())
print(employee.show_salary())
print(employee.plus_salary())