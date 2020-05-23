# !/usr/bin/python
# -*- coding: utf-8 -*-

# Task 6
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

# import math

while True:
    goal_dist = input('Введите вашу цель (в км)?\n')
    if goal_dist.isdigit():
        goal_dist = int(goal_dist)
        print('Ваша цель - ', goal_dist,'км. \n')
        break
    else:
        print('Введите повторно корректное расстояние в километрах. \n')
while True:
    first_day_dist = input('Введите расстояние в км, которое Вы способны пробежать сейчас?\n')
    if first_day_dist.isdigit():
        first_day_dist = int(first_day_dist)
        print('Вы способны бегать на дистанцию ', first_day_dist,'км. \n')
        break
    else:
        print('Введите повторно корректное расстояние в километрах.')

# Дополнительная проверка корректности цели
if goal_dist <= first_day_dist:
    print('Вы слишком круты для этой задачи.. Подумайте о новых амбициозных целях и возвращайтесь к нам! ;)  \n')
else:
    rate = 0.1 # скорость прогрессирования в беге = 10%
    progress = 1 + rate
    # первый способ был: из формулы сложного путем логорифмирования вычислить необходимое время до достижения нужного результата
    # Time = int(math.log10(goal_dist/first_day_dist,)/math.log10(progress)) + 1
    # print('Для достижения поставленной цели, Вам потребуется дней:', Time,' (при сохранении скорости прогресса). \n')
    
    # второй вариант решения - использование цикла while ( = без логарифмирования)
    day_count = 0 # счетчик дней
    
    while True:
        distance = first_day_dist # вычисляем прогресс по дням
        distance = distance * (progress ** day_count) # формула сложного процента
        print('День #', day_count,', Текущий прогресс - ',distance,"км")
        if distance > goal_dist:
            Time = int(day_count)
            print('Для достижения поставленной цели, Вам потребуется дней:', Time,' (при сохранении скорости прогресса). \n')
            break
        else:
            day_count += 1 # инкремент
        