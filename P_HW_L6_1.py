# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time

class Trafficlight():
    __color = ["\033[41mкрасный", "\033[43mжелтый", "\033[42mзеленый"]

    def __init__(self, t):
        self.time = t

    def running(self):
        for x in range(len(Trafficlight.__color)):
            print(Trafficlight.__color[x])
            time.sleep(self.time[x])

c = input("Какой свет включить? ")
a = Trafficlight([7, 2, 5])
sf_colors = [a._Trafficlight__color[i][5:] for i in range(len(a._Trafficlight__color))]
if c in sf_colors:
    print(f"у светофора есть {c} свет, включаю светофор по порядку")
    a.running()
else:
    print(f"у светофора нет такого света")


#  скрипт без проверки цвета

# import time
#
# class Trafficlight():
#     __color = ["\033[41mкрасный", "\033[43mжелтый", "\033[42mзеленый"]
#
#     def __init__(self, t):
#         self.time = t
#
#     def running(self):
#         for x in range(len(Trafficlight.__color)):
#             print(Trafficlight.__color[x])
#             time.sleep(self.time[x])
#
# n = int(input("Сколько раз включить красный: "))
# for i in range(n):
#     a = Trafficlight([7, 2, 5])
#     a.running()


