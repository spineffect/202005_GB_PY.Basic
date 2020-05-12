# !/usr/bin/python
# -*- coding: utf-8 -*-

# Task 4
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

while True:
    numb1 = input('Введите целое положительное число: ')
    str_n = numb1
    if numb1.isdigit():
        numb1 = int(numb1)
        print('вы ввели число - ', numb1,'\n')
        if numb1 > 0:
            break
        else:
            print('Вы ввели число за пределами предложенного диапазона (меньше 1). Поторите попытку. ')
    else:
        print('Вы ввели' , numb1, 'Это неверный ввод. Введите число повторно. ' )

word_letters = list(str_n)  # переводим слово в список (побуквенно)
max_numb = int(word_letters[-1]) # устанавливаем начальные условия для поиска (макс; индекс)
idx = 1
while True:
    if idx == len(word_letters):
        print('Максимум: ', max_numb)
        break
    else:
        k = int(word_letters[idx-1])
        print('Значение из списка: ', k, '(шаг  ', idx,' из ',len(word_letters),')')
        if k > max_numb:
            max_numb = k
            print('!!! Вывлено максимальное значение:', max_numb,' (на шаге ',
                  idx,' из ',len(word_letters),')')
            idx = idx + 1
            if max_numb == 9:
                print('Максимум: ', max_numb)
                break
            else:
                continue
        else:
            idx = idx + 1