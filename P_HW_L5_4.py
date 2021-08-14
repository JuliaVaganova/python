# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_list = open("textmy_4.txt", "w+", encoding="utf-8")
with open("text_4.txt", "r+", encoding="utf-8") as eng_list:
    my_dict = {"One":"Oдин", "Two":"Два", "Three":"Три", "Four":"Четыре"}
    lines = eng_list.readlines()
    #new_lines = []
    for line in lines:
        line = line.split(" ")
        line[0] = my_dict[line[0]]
        new_line=" ".join(line)
        rus_list.writelines(new_line)
rus_list.close()