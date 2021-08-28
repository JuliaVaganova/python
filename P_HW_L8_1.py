#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    # def __init__(self, date):
    #     self.date = date

    @classmethod
    def transform(cls, param):
        parts = param.split("-")
        return Data.validator(int(parts[0]), int(parts[1]), int(parts[2]))

    @staticmethod
    def validator(d, m, y):
        print(f"день {str(d).zfill(2)}") if 1 <= d <= 30 else print("Ошибка! такого дня нет")
        print(f"месяц {str(m).zfill(2)}") if 1 <= m <= 12 else print("Ошибка! такого месяца нет")
        print(f"год {str(y).zfill(4)}") if 1 <= y <= 9999 else print("Ошибка! такого года нет")


userdate = input("Ведите дату в формате dd-mm-yyyy: ")
a = Data.transform(userdate)
# a = Data(userdate)
