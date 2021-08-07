#5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.


def f_count(sum_line, sum_total):
    sum_line = 0
    sum_total = 0
    finish = False
    while finish != True:
        line=input("Введите цифры через пробел или Q для выхода: ").split()
        sum_line = 0
        i = 0
        while i < len(line):
            if line[i] == "Q" or line[i] == "q":
                finish = True
                break
            else:
                try:
                    line[i]=int(line[i])
                    sum_line=sum_line+line[i]
                except ValueError:
                    print("ввели букву")
            i += 1
        sum_total=sum_total + sum_line
        print("Сумма по строке / итого: ", sum_line, "/", sum_total)
    else:
        print ("Конец!")

sum_line = None
sum_total = None
f_count(sum_line, sum_total)
