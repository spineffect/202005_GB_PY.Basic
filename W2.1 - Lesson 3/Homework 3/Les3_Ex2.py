'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
def print_ud(data_list):    # на входе функции получаем словарь
    #Формируем данные для печати, сцепляя их в одну строковую переменную с разделитетем "; "
    printed_str = ''
    if type(data_list) is dict:     # проверка типа входящих данных
        for key in data_list:
            printed_str += str(data_list[key]) + '; '
    elif (type(data_list) is list) or (type(data_list) is tuple):   # проверка типа входящих данных
        for el in user_data_list:
            printed_str += str(el) + '; '
    else:
        printed_str = 'Функция не может быть выполнена, по причине некорректных исходных данных'
    print(printed_str)
    return

user_data_list = {
    'Имя': 'Иван',
    'Фамилия': 'Иванов',
    'год рождения': 1980,
    'город проживания': 'Москва',
    'e-mail': 'ivanov@mail.net',
    'телефон': '+1 234 567-8910'
}
print(type(user_data_list))
print_ud(user_data_list)

user_data_list = ("Иванка", "Иванова", 1982, "Иваново", "ivanka@invanovo.net", '+1 234 567-8910')
print(type(user_data_list))
print_ud(user_data_list)

user_data_list = "Иванов, Иван, 1980, Москва, ..., .."
print(type(user_data_list))
print_ud(user_data_list)






