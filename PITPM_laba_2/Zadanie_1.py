class Car:
    color = None  # цвет автомобиля
    fuel = None  # количество топлива
    wheels = None  # колёса
    body_type = None  # вид кузова
    engine_capacity = None  # объём двигателя

    def inf_car(self):
        print(myCar.color)
        print(myCar.fuel)
        print(myCar.wheels)
        print(myCar.body_type)
        print(myCar.engine_capacity)

    def go(self):
        # Команда ехать:
        pass

    def turn(self):
        # Команда поворачивать:
        pass

    def stop(self):
        # Команда остановиться:
        pass

myCar = Car()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.wheels = 'kruglie'  # вид колёс
myCar.body_type = 'sedan'  # вид кузова
myCar.engine_capacity = '250'  # объём двигателя

myCar.inf_car()
myCar.go()
myCar.turn()
myCar.stop()