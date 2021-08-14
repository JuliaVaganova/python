# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

file_calc = open("file_5.txt", "w+")
a = 20
sum = 0
digits = [str(randint(1, a)) for i in range(1, a)]
digits_str = " ".join(digits)
file_calc.write(digits_str)
file_calc.seek(0)
str_out = file_calc.read()
print("Числа в файле: ", str_out)
list_out = str_out.split(" ")
for i in list_out:
    i = int(i)
    sum += i
print("Сумма чисел в файле: ", sum)
file_calc.close()
