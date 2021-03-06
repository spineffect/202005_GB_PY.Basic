'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''
import random

# решение первым способом
a, b = random.randint(1, 99), -random.randint(1, 99)
def my_func_1(x, y):
    return x**y
print(f'func_1: {a} в степени {b} равно {my_func_1(a,b)}')

# решение вторым способом
# a, b = random.randint(1, 99), -random.randint(1, 99)
def my_func_2(x, y):
    res = 1
    while y != 0:
        res /= x
        y += 1
    return res
print(f'func_2: {a} в степени {b} равно {my_func_2(a,b)}')