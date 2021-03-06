# !/usr/bin/python
# -*- coding: utf-8 -*-
# # Task 5
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника

while True:
    revenue = input('Введите вашу выручку (в тыс.р)? \n')
    if revenue.isdigit():
        revenue = int(revenue)
        print('Ваша выручка - ', revenue,'(в тыс.р) \n')
        break
    else:
        print('Введите повторно корректное число. \n')

while True:
    costs = input('Введите издержки (в тыс.р)?\n')
    if costs.isdigit():
        costs = int(costs)
        print('Ваши издержки - ', costs,'(в тыс.р) \n')
        break
    else:
        print('Введите повторно корректное число. \n')

balance = revenue - costs

if costs > revenue:
    print ('Дела плохи, Ваш убыток составил ',balance,' тыс.р.! Обратитель с финансовому консультанту!')
else:
    print ('Так держать, Ваш доход составил ',balance,' тыс.р.!')
    prof_ratio = 100 * revenue / costs
    print('Рентабельность, % : ', prof_ratio)
    while True:
        empl_amnt = input('Какова численность компании (чел)?\n')
        if empl_amnt.isdigit():
            empl_amnt = int(empl_amnt)
            break
        else:
            print('Введите повторно корректное число. \n')
    capacity = revenue / empl_amnt
    print('производительность труда - ', capacity, '(тыс.р/чел) \n')