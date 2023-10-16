class User:
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Employee(User):
    def setYear(self, year):
        self._year = year

    def getYear(self):
        return self._year

class Programmer(Employee):
    def setSkill(self, skill):
        self._skill = skill

    def getSkill(self):
        return self._skill

class Designer(Employee):
    def setStyle(self, style):
        self._style = style

    def getStyle(self):
        return self._style

programmer = Programmer()
designer = Designer()

designer.setName('Mai')
designer.setYear(12)
designer.setStyle('Nemo')
programmer.setSkill('Midle')

print(designer.getName(), designer.getYear(), designer.getStyle(), programmer.getSkill())