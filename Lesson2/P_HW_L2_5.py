#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

initial_list = [6, 5, 3, 3, 2]
print ("Текущий рейтинг: ")
print(*initial_list, sep=', ')
new_el = int(input("Введите новый элемент рейтинга: "))
min_el = min (initial_list)
max_el = max (initial_list)
equals_num = initial_list.count(new_el)
for i in initial_list:
    if new_el < min_el:
        initial_list.append(new_el)
        break
    elif new_el > max_el:
        initial_list.insert(0, new_el)
        break
    else:
        index_now=initial_list.index(new_el)
        initial_list.insert((equals_num+index_now), new_el)
        break
print("Новый рейтинг: ")
print(*initial_list, sep=', ')

