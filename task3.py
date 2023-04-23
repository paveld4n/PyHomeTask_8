# Задача 3
# Задание на закрепление знаний по модулю yaml.
#  Написать скрипт, автоматизирующий сохранение данных
#  в файле YAML-формата.
# Для этого:

# Подготовить данные для записи в виде словаря, в котором
# первому ключу соответствует список, второму — целое число,
# третьему — вложенный словарь, где значение каждого ключа —
# это целое число с юникод-символом, отсутствующим в кодировке
# ASCII(например, €);

# Реализовать сохранение данных в файл формата YAML — например,
# в файл file.yaml. При этом обеспечить стилизацию файла с помощью
# параметра default_flow_style, а также установить возможность работы
# с юникодом: allow_unicode = True;

# Реализовать считывание данных из созданного файла и проверить,
# совпадают ли они с исходными.

import yaml

def writeDict(dict, file):
    with open(file, "w", encoding="utf-8") as f_n:
        yaml.dump(dict, f_n, default_flow_style=False, allow_unicode=True)
    
    with open(file, "r", encoding="utf-8") as f_r:
        print(yaml.safe_load(f_r) == dict)

    
my_dict = {
    "1111€": ["Sony", "Panasonic", "Huawei", "Matsushita"],
    "2222€": 5000,
    "3333€": {
        "first": [1,2,3,4],
        "second": 6789,
        "third": "popa"

    }
}

writeDict(my_dict, "file.yaml")