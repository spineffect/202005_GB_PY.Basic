# !/usr/bin/python
# -*- coding: utf-8 -*-

# Task 3
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

while True:
    numb1 = input('Введите целое число от 1 до 9?\n')
    str_n = numb1 # переменная для альтернативного варианта решения
    if numb1.isdigit():
        numb1 = int(numb1)
        print('вы ввели число - ', numb1,'\n')
        if numb1 >= 1 and numb1 < 10:
            break
        else:
            print('Вы ввели число за пределами предложенного диапазона (от 1 до 9). \n')
else:
    print('Вы ввели' , numb1, 'Введенные симовлы имею тип ', type(numb1),'\n', 'Неверный ввод. Введите число повторно. \n')
print(numb1)

# арифметический способ решения
numb_nn = 11 * numb1
numb_nnn = 111 * numb1
var_sum = numb1 + numb_nn + numb_nnn
print('Ответ: ',numb1,' + ',numb_nn,' + ',numb_nnn,' = ', var_sum)

# символьно-арифметический способ решения (альтернативный)
print('Альтернативный способ расчета: слогаемых NN и NNN, как суммы символьных выражений ===>...')
numb_nn = str_n + str_n
numb_nn = int(numb_nn)
numb_nnn = str_n + str_n + str_n
numb_nnn = int(numb_nnn)
str_n = int(str_n)
var_sum = str_n + numb_nn + numb_nnn
print('Ответ (альтернативный способ): ',str_n,' + ',numb_nn,' + ',numb_nnn,' = ', var_sum,'\n')