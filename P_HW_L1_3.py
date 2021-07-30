# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Короткий вариант с фиксированным количеством (3 слагаемых) n+nn+nnn
usernum = input('Введите целое положительное число: ')
num = int(usernum) + int(usernum + usernum) + int(usernum + usernum + usernum)
print("Результат", num)
print()

# Вариант с любым количеством слагаемых n+nn+nnn+....
usernum = input('Введите целое положительное число: ')
seq = int(input('Сколько чисел с увеличением на порядок сложить?: '))
num = str()
i = 0
finalres = 0
while i <= seq - 1:
    num = num + usernum
    finalres = finalres + int(num)
    i += 1
print("Результат: ", finalres)
