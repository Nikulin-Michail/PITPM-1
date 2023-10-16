class Employee:
    def setName(self, name):
        self.name = name

    def getName(self):
        print(self.name)

    def setAge(self, age):
        self.age = age

    def getAge(self):
        print(self.age)

class Student(Employee):
    def setAge(self, age):
        if 18 < age < 65:
            self.age = age
        else:
            raise Exception("student stariy")

student = Student()

student.setName("john")
student.setAge(23)

student.getName()
student.getAge()