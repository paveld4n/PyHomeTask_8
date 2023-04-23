# Задача 1
# Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
#  info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
#  системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
#  Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции
#  создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета
#  в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также
#  оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
#  через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().'''


import re
import csv


def get_data(list_1):
    prod_list = []
    name_list = []
    code_list = []
    type_list = []
    main_data = [["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]]

    for file in list_1:
        f_data = open(file)
        for row in f_data:
            row = row.rstrip () #Удаляем пробелы в конце строки
            if re.match("Изготовитель системы", row):
                prod_list.append(re.search(r'(Изготовитель системы).\s*(.*)', row).group(2))
            elif re.match("Название ОС", row):
                name_list.append(re.search(r"(Название ОС).\s*(.*)", row).group(2))
            elif re.match("Код продукта", row):
                code_list.append(re.search(r"(Код продукта).\s*(.*)", row).group(2))
            elif re.match("Тип системы", row):
                type_list.append(re.search(r"(Тип системы).\s*(.*)", row).group(2))

    for i in range(len(list_1)):
        main_data.append([prod_list[i], name_list[i], code_list[i], type_list[i]])
    return main_data

def write_to_csv(file, data):
    with open(file, "w", encoding="utf-16") as f_n:
        f_n_wr = csv.writer(f_n)
        for row in data:
            f_n_wr.writerow(row)




res = get_data(["info_1.txt", "info_2.txt", "info_3.txt"])
write_to_csv("rezult_file.csv", res)

with open("rezult_file.csv", "r", encoding="utf-16") as f_n:
    print(f_n.read())