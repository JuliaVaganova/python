# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def funk_div(dig_1, dig_2):
    return dig_1 / dig_2

while True:
    try:
        num1 = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Вы ввели не числo. Попробуйте еще раз.")
while True:
    num2 = input("Введите второе число: ")
    try:
        num1 = float(num1)
        num2 = float(num2)
        num2 != 0
        print(f"Результат деления числа {num1} на число {num2} равен {funk_div(num1, num2):.4f}")
        break
    except ValueError:
        print("Вы ввели не числo. Попробуйте еще раз.")
    except ZeroDivisionError:
        print("Делить на ноль нельзя")
else:
    print("Ошибка")


