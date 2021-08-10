# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.


def fact(n):
    n_fact = 1
    for i in range(0, n):
        n_fact = n_fact * (i + 1)
        yield n_fact


while True:
    n = input("Сколько факториалов вычислить: ")
    try:
        n = int(n)
        if n <= 0:
            raise ValueError
        for el in fact(n):
            print(el)
        break
    except ValueError:
        print("Ошибка. Введите целое положительное число.")
