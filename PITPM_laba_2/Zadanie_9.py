class Student:
    name = 'Alex'
    surname = 'Mirniy'

    def show(self):
        return self.name, self.surname

student = Student()

print(student.name)
print(student.surname)