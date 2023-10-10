class Student:
  name = 'Makar'
  surname = 'Smirnov'

  def show(self):
    return self.cape(self.name[0] + " " + self.surname[0])

  def cape(self, stri):
    return stri.upper()

student = Student()

print(student.show())