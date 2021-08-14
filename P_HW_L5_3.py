# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("text_3.txt", "r", encoding="utf-8") as salary_file:
    salary_file.seek(0)
    l_low = []
    total_emp = 0
    total_sum = 0
    content = salary_file.read().split("\n")
    for pair in content:
        pair = pair.split(" ")
        total_emp = total_emp+1
        total_sum = total_sum + float(pair[1])
        if float(pair[1]) < 20000:
            l_low.append(pair[0])
    av = total_sum/total_emp
    print("Оклад менее 20000 у сотрудников:", ', '.join(l_low), "\nCредний оклад", av)


