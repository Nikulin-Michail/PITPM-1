class Employee:
    def show(self, name, salary):
        return name + ' ' + salary


employee = Employee()

print(employee.show('Gleb', '10000'))
