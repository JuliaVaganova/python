#3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class My_exc:
    def __init__(self, param):
        self.param = param

    def check(self):
        a = "".join((self.param[1:]).split("."))
        if self.param.isdigit() == True:
            return f"{self.param}"
        elif a.isdigit() == True and (self.param.count(".") <= 1):
            if self.param[0] == "-" or self.param[0].isdigit() or self.param[0] == ".":
                return f"{self.param}"

my_list = []
print("Введите числa/enter - конец ввода чисел: ")
while True:
    num = input()
    if num == "":
        break
    else:
        x = My_exc(num)
        if x.check() != None:
             my_list.append(num)
        else:
             print("введено не число или не верный формат, продолжите ввод чисел или enter для окончания")
print("Список чисел: ", ", ".join(my_list))


