# !/usr/bin/python
# -*- coding: utf-8 -*-

# Task 2
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

while True:
    time_s = input('Введите время в секундах?\n')
    if time_s.isdigit():
            time_s = int(time_s)
            print('вы ввели число - ', time_s,'\n')
            break
    else:
        print('Вы ввели' , time_s, 'Это не число (Введенные симовлы имею тип ', type(time_s),')\n', 'Введите время в секундах повторно. \n')

# вычисления количества часов
time_h = time_s / 3600 
time_h = int(time_h) # отсекаем целочисленную часть числа
# вычисления остатка в минутах
time_m = (time_s - time_h * 3600) / 60
time_m = int(time_m) # отсекаем целочисленную часть числа
# остаток в секундах
time_s1 = time_s - time_m * 60 - time_h * 3600
print(time_s,' секунд -->> ... (чч:мм:cc) ... -->>  ', time_h,':', time_m,':', time_s1,'\n')