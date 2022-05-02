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


def make_analysis(words):
    data = {}
    for word in words:
        data[len(word)] = data.get(len(word), 0) + 1
    return data


def make_analysis_list(dictionary):
    array = []
    for key, value in dictionary.items():
        s = ''
        s = 'Количество слов, длина которых равна ' + str(key) + ' символов: ' + str(value)
        array.append(s)
    return array


name_of_file = input("Введите название файла или путь к нему: ")

if check_file(name_of_file):
    with open(name_of_file, 'r', encoding='utf-8') as input_file:

        if is_it_empty(input_file):
            original_words = []
            word_division(input_file, original_words)
            update_words = updating_words(original_words)
            update_words = list(filter(lambda word: word.isalpha(), update_words))
            insert_sort(update_words)
            # print(*update_words, sep='\n')
        else:
            print("Этот файл пуст...")

with open('result.txt', 'w', encoding='utf-8') as output_file:
    for word in update_words:
        print(word, file=output_file)

analysis = make_analysis(update_words)
analysis_list = make_analysis_list(analysis)

with open('analysis.txt', 'w', encoding='utf-8') as analysis_file:
    for value in analysis_list:
        print(value, file=analysis_file)