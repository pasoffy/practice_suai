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


name_of_file = input("Введите название файла или путь к нему: ")

if check_file(name_of_file):
    with open(name_of_file, 'r', encoding='utf-8') as input_file:

        if is_it_empty(input_file):
            print("its ok")
        else:
            print("its not ok")

