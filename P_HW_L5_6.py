# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
my_file = open("text_6.txt", "r+", encoding="utf-8")

course = []
hours = []
while True:
    lineinfile = my_file.readline()
    if lineinfile != "":
        line = lineinfile.split(" ")
        #print("вся строка", line, type(line))
        new_list = []
        sum_hours = 0
        for word in line:
            a = [word[x] for x in range(len(word)) if word[x].isdigit()]
            a = "".join(a)
            if a.isdigit():
                new_list.append(int(a))
                sum_hours=sum(new_list)
        course.append(line[0])
        hours.append(sum_hours)
        #print("сумма",sum_hours)
    if not lineinfile:
         break

dict_lessons = dict(zip(course, hours))
print(dict_lessons)

my_file.close()

""""
считает сумму на 1 строку
a = ("Math: 10(л) 50(пр) -")
line = a.split(" ")
print("вся строка", line, type(line))
print(len(line))
new_list = []
sum_hours = 0
for word in line:
    print ("слово", word)
    a = [word[x] for x in range(len(word)) if word[x].isdigit()]
    a = "".join(a)
    print("число в слове", a, type(a))
    if a.isdigit():
        new_list.append(int(a))
        print(new_list)
        sum_hours=sum(new_list)
print("сумма",sum_hours)
"""





