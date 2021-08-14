#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_file = open("file_1.txt", "w+", encoding="utf-8")
while True:
    user_str = input(f"Введите данные: ")
    user_file.writelines(f'{user_str}\n')
    if len(user_str) == 0:
        break
user_file.seek(0)
out_file=user_file.readlines()
print("\nВ файле лежит: ")
for line in out_file:
    print(line, end='')
user_file.close()

