import string
import os

def find_longest_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Удаляем знаки препинания и спецсимволы
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    # Разделяем текст на слова
    words = cleaned_text.split()

    # Находим максимальную длину слова
    max_length = max(len(word) for word in words)

    # Находим все слова максимальной длины
    longest_words = [word for word in words if len(word) == max_length]

    return longest_words


# Имя файла

filename = input()

if os.path.getsize(filename):
    # Поиск и вывод слов максимальной длины
    longest_words = find_longest_words(filename)
    for word in longest_words:
        print(word)
else:
    print('Файл пуст!')
