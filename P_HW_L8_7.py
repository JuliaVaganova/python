# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Comp_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.znak = ["-", "+"]

    def __add__(self, other):
        znak_str = self.znak[0] if (self.b + other.b) < 0 else self.znak[1]
        return f'Сумма = {self.a + other.a} {znak_str} {abs(self.b + other.b)}*j'

    def __mul__(self, other):
        znak_str = self.znak[0] if (self.a * other.b + self.b * other.a) < 0 else self.znak[1]
        return f'Произведение = {self.a * other.a - self.b * other.b} {znak_str} {abs(self.a * other.b + self.b * other.a)}*j'


z_1 = Comp_num(3, 1)
z_2 = Comp_num(2, -3)

print(z_1 + z_2)
print(z_1 * z_2)