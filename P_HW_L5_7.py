# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    total_profit = 0
    i = 0
    key_pl = []
    value_pl = []
    av_key = ["Средняя прибыль"]
    av_value = []
    while True:
        lineinfile = my_file.readline()
        if lineinfile != "":
            line = lineinfile.split(" ")
            key_pl.append(line[0])
            profit = int(line[2]) - int(line[3])
            value_pl.append(profit)
            if profit > 0:
                i += 1
                total_profit += profit
        if not lineinfile:
            break
    av_value.append(total_profit / i)
    final_list = [dict(zip(key_pl, value_pl)), dict(zip(av_key, av_value))]
    print(final_list)

with open("file_7.json", "w", encoding="utf-8") as my_jsonfile:
    json.dump(final_list, my_jsonfile, ensure_ascii=False)
