# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    total = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        Clothes.total += self.calc + other.calc
        return Suit(0)

    def __str__(self):
        total = Clothes.total
        Clothes.total = 0
        return f"Нужно ткани на все пальто и костюмы: {total} м"


class Coat(Clothes):
    @property
    def calc(self):
        return round(self.param / 6.5) + 0.5


class Suit(Clothes):
    @property
    def calc(self):
        return round((2 * self.param + 0.3) / 100)


a_1 = Coat(42)
a_2 = Suit(180)
a_3 = Coat(46)
a_4 = Suit(190)

print(a_1 + a_2 + a_3 + a_4)
