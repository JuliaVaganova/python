# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_funk(a, b, c):
    return a + b + c - min(a, b, c)


print("Введите три числа:")
print(my_funk(int(input()), int(input()), int(input())))
