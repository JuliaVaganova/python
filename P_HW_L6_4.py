# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.high_speed = "Скорость превышена"

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась\n")

    def turn(self):
        direction = ["направо", "налево", "на разворот"]
        print(f"{self.color} {self.name} повернула {random.choice(direction)}")

    def show_speed(self):
        print(f"у {self.color} {self.name} скорость {self.speed}")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"{self.color} {self.name} - городская машина")
    def show_speed(self):
        print(f"у {self.color} {self.name} скорость {self.speed}")
        if self.speed > 60:
            print(self.high_speed)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"{self.color} {self.name} - спортивная машина")
        # if self.speed > 60:
        #     print(self.high_speed)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f"{self.color} {self.name} - рабочая машина")
    def show_speed(self):
        print(f"у {self.color} {self.name} скорость {self.speed}")
        if self.speed > 40:
            print(self.high_speed)

class Police(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def police(self):
        if self.is_police is True:
            print(f"{self.color} {self.name} - это полицейская машина")
        else:
            print(f"{self.color} {self.name} - это не полицейская машина")

car_1 = SportCar(180, "красная", "Ferrari", False)
car_1.go()
car_1.show_speed()
car_1.turn()
car_1.stop()

car_2 = WorkCar(50, "желтый", "ВАЗ", False)
car_2.go()
car_2.show_speed()
car_2.turn()
car_2.stop()

car_3 = TownCar(70, "белая", "Audi", False)
car_3.go()
car_3.show_speed()
car_3.turn()
car_3.stop()

car_4 = Police(100, "черная", "Lada", True)
car_4.go()
car_4.police()
car_4.show_speed()
car_4.turn()
car_4.stop()

print(car_1.is_police)
print(car_2.speed)
print(car_3.color)
print(car_4.name)
