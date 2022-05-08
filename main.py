import os
import string
import time


def check_file(name):
    try:
        if os.path.getsize(name) > 0:        # возвращает размер файла в байтах
            return True
        else:
            print("Это пустой файл")
            return False

    except OSError:                        # обработка исключения (файла с заданным именем не существует)
        print("Невозможно открыть файл!")
        return False


def is_it_empty(file):
    file.seek(0)
    for line in file:
        if line != '\n' and line != '':                   # проверка на то, есть ли в файле текст
            return True
    return False


def word_division(file, words):
    input_file.seek(0)                  # устанавливаем курсор в начало файла
    for line in file:
        words.extend(line.strip().split())    # разбиваем текст на слова, которые записываем в массив


def updating_words(words):
    for i in range(len(words)):
        word = words.pop(i)
        new_word = ''
        for char in word:
            if char in string.punctuation or char in string.digits:
                continue                   # удаляем знаки препинания и цифры
            else:
                new_word += char
        words.insert(i, new_word)
    return words


def insert_sort(words):                                           # функция сортировки вставками
    for i in range(1, len(words)):                                # цикл для прохода по неотсортированной части массива
        for j in range(i, 0, -1):
            if len(words[j]) > len(words[j - 1]):
                words[j - 1], words[j] = words[j], words[j - 1]  # меняем местами бОльший элемент с меньшими
            else:
                break


def make_analysis(words):                                       # функция создания словаря, ключами которого являются
    data = {}                                                   # длины слов, а значениями количество слов
    for word in words:                                          # соответсвующей длины
        data[len(word)] = data.get(len(word), 0) + 1            # при обращении к несуществующему ключу, метод get()
    return data                                                 # возвращает значение переданное в качестве второго
                                                                # аргумента


def make_analysis_list(dictionary):                            # записываем значения из словаря в строки, которые
    array = []                                                 # в свою очередь добавляем в массив для последующей
    for key, value in dictionary.items():                      # записи в файл
        s = ''
        if key == 0:
            continue
        else:
            s = 'Количество слов, длина которых равна ' + str(key) + ' символов: ' + str(value)
            array.append(s)
    return array


name_of_file = input("Введите название файла или путь к нему: ")

start_time = time.time()
if check_file(name_of_file):
    with open(name_of_file, 'r') as input_file:

        if is_it_empty(input_file):
            original_words = []
            word_division(input_file, original_words)

            print("Вариант 21: Сортировка вставками в обратном порядке по длине слова, цифры игнорируются")
            print("Введенный текст:", *original_words)
            print("Всего слов:", len(original_words))

            original_words_copy = original_words.copy()
            update_words = updating_words(original_words)
            insert_sort(update_words)

            with open('result.txt', 'w+', encoding='utf-8') as output_file:
                for word in update_words:
                    print(word, file=output_file)  # записываем в файл отсортированные слова

                if not is_it_empty(output_file):
                    output_file.seek(0)
                    print("А сортировать-то нечего...", file=output_file)

            analysis = make_analysis(update_words)
            analysis_list = make_analysis_list(analysis)

            with open('analysis.txt', 'w+', encoding='utf-8') as analysis_file:
                for value in analysis_list:
                    print(value, file=analysis_file)  # записываем в файл анализ длдин слов
                analysis_file.seek(0)
                if analysis_file.readlines() == []:
                    print("В исходном файле не было найдено слов...", file=analysis_file)
                else:
                    print("Вариант 21: Сортировка вставками в обратном порядке по длине слова, цифры игнорируются",
                          file=analysis_file)
                    print("Введенный текст:", *original_words_copy, file=analysis_file)
                    print("Всего слов:", len(original_words_copy), file=analysis_file)
                    print("--- %s seconds ---" % (time.time() - start_time), file=analysis_file)
            if analysis_list == []:
                print("В исходном файле не было найдено слов...")
            else:
                print(*analysis_list, sep='\n')
        else:
            print("Этот файл пуст...")
print("%s секунд" % (time.time() - start_time))
