#2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("textmy_2.txt", "r", encoding="utf-8") as user_file:
    # num_lines = 0
    # print("Введите несколько строк данных. Конец ввода - пустая строка")
    # while True:
    #     user_data = input('ввод: ')
    #     user_file.writelines(f'{user_data}\n')
    #     if user_data == "":
    #         break
    user_file.seek(0)
    line_file = user_file.readlines()
    print(f"\nВ файле: ", len(line_file), "строк\n")
    for i in range(len(line_file)):
        num_words = len(line_file[i].split())
        print(f"Строка {i+1} содержит {num_words} слов: {line_file[i]}", end="")
