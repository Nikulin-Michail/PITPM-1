class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return (f"{self.name} {self.surname}")

    def get_initials(self):
        return f"{self.name[0]}.{self.surname[0]}."


class Employee(Person):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self.salary = salary

    # Геттер и сеттер зарплаты
    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    # Геттер и сеттер имени
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Геттер и сеттер фамилии
    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self.surname = new_surname


employee = Employee("Timyr", "Tamerlan", 500)# Изначальные данные
print(employee.get_fullname())
print(employee.get_initials())


# Замена

print(employee.get_salary(), end=" => ")
employee.set_salary(600)
print(employee.get_salary())

print(employee.get_name(), end=" => ")
employee.set_name("Simen")
print(employee.get_name())


print(employee.get_surname(), end=" => ")
employee.set_surname("Bych")
print(employee.get_surname())