#5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title="Эскиз."):
        self.title = title

    def draw(self):
        print(self.title, "Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(self.title, "Отрисовка ручкой")

class Handle(Stationery):
    def draw(self):
        print(self.title, "Отрисовка маркером")

class Pencil(Stationery):
    def draw(self):
        print(self.title, "Отрисовка карандашом")

any_st = Stationery()
any_st.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
marker = Handle()
marker.draw()





