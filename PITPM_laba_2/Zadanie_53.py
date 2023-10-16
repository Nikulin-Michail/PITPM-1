class Circle:
    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return 3.14 * self.__radius ** 2

    def getCircumference(self):
        return 2 * 3.14 * self.__radius

circle = Circle()

circle.setRadius(5)

print(circle.getArea())
print(circle.getCircumference())