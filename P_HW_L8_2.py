#2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class Div_by_zero(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    try:
        num_1 = float(input("\nВедите первое число: "))
        num_2 = float(input("Ведите второе число: "))
        if num_2 == 0:
            raise Div_by_zero("Вы ввели второе число 0, на ноль делить нельзя!")
    except ValueError:
        print("Вы ввели не число")
    except Div_by_zero as err_2:
        print(err_2)
    else:
        print(f"Результат деления: {round(num_1/num_2, 2)}")
        break

# Вариант 2

# class Div_by_zero(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# while True:
#     num_1 = input("\nВедите первое число: "))
#     if type(
#     num_2 = input("Ведите второе число: "))
#     if num_2 == 0:
#         print(Div_by_zero("Вы ввели второе число 0, на ноль делить нельзя!"))
#     else:
#         print(f"Результат деления: {round(num_1/num_2, 2)}")
#         break
