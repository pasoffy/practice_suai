import os


def check_file(name):
    try:
        if os.path.getsize(name) > 0:
            return True
        else:
            print("Это пустой файл")
            return False

    except OSError:
        print("Невозможно открыть файл!")
        return False


def is_it_empty(file):
    return file.readline() != '\n'


def word_division(file, words):
    input_file.seek(0)
    for line in file:
        words.extend(line.strip().split())


def updating_words(words):
    for i in range(len(words)):
        word = words.pop(i)
        punctuations = ['.', ',', '!', '?', '-', '%', ';', ':', '/', '"', "'"]
        for mark in punctuations:
            word = word.strip(mark)
        words.insert(i, word)
    return words


def insert_sort(words):
    for i in range(1, len(words)):
        for j in range(i, 0, -1):
            if len(words[j]) > len(words[j - 1]):
                words[j - 1], words[j] = words[j], words[j - 1]
            else:
                break


name_of_file = input("Введите название файла или путь к нему: ")

if check_file(name_of_file):
    with open(name_of_file, 'r', encoding='utf-8') as input_file:

        if is_it_empty(input_file):
            original_words = []
            word_division(input_file, original_words)
            update_words = updating_words(original_words)
            update_words = list(filter(lambda word: word.isalpha(), update_words))
            insert_sort(update_words)
            print(*update_words, sep='\n')
        else:
            print("Этот файл пуст...")

