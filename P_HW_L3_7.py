# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
# для проверки  nice авп ъghj jапро hjjпаро вапрghgh cool

""" Функция проверяет слово на латиницу и, если все буквы латиница, возвращает слово с большой буквы """


def f_sent(word):
    global new_word
    new_word = str()
    for i in range(len(word)):
        if ord(word[i]) >= 97 and ord(word[i]) <= 122:
            new_word = word.title()
        else:
            new_word = None
            break


# Применяет функцию к каждому слову в предложении

print("На примере: 'ъghj jапро hjjпаро вапрghgh cool'")
sentence = "nice авп ъghj jапро hjjпаро вапрghgh cool".split()
new_sentence = []
for i in sentence:
    f_sent(i)
    if new_word is not None:
        new_sentence.append(new_word)
print(" ".join(new_sentence))
