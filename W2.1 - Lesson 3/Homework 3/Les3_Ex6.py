'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
'''
def int_func(words):
    words = words.lower()      # на всякий случай, если при вводе "закрались" заглавные буквы
    words = words.capitalize()
    return words

def sep_words(words):
    # изменяем каждое слово
    words = words.split(" ")
    for el in words[:]:
        words[words.index(el)] = int_func(el)
    # cклеиваем в строку для печати
    text = ""
    for el in words[:]:
        text += str(el) + " "
    return text

word_list = 'lorem ipSUm doLOR sIt aMEt, consectetur adipiscing elit'
print(f'Было:\n{word_list}')

print(f'Стало:\n{sep_words(word_list)}')