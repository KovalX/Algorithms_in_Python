"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


class TownCar:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина {} поехала".format(self.name))

    def stop(self):
        print("Машина {} остановилась".format(self.name))

    def turn(self, direction):
        print("Машина {} повернула {}".format(self.name, direction))


class SportCar:
    __slots__ = ["name", "color", "speed", "is_police"]

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина {} поехала".format(self.name))

    def stop(self):
        print("Машина {} остановилась".format(self.name))

    def turn(self, direction):
        print("Машина {} повернула {}".format(self.name, direction))


class WorkCar:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина {} поехала".format(self.name))

    def stop(self):
        print("Машина {} остановилась".format(self.name))

    def turn(self, direction):
        print("Машина {} повернула {}".format(self.name, direction))


class PoliceCar:
    def __init__(self, name, color, speed, is_police=True):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Машина {} поехала".format(self.name))

    def stop(self):
        print("Машина {} остановилась".format(self.name))

    def turn(self, direction):
        print("Машина {} повернула {}".format(self.name, direction))


my_car = WorkCar("Toyota Corolla", "black", 140)
print(my_car.__dict__)
print(asizeof.asizeof(my_car))
# my_car.year = 2010
# print(my_car.year)
# print(asizeof.asizeof(my_car))


supercar = SportCar("Lamborghini", "red", 370)
print(asizeof.asizeof(supercar))
# print(supercar.__dict__)
# supercar.year = 2018