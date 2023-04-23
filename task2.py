# Задача 2.
# Задание на закрепление знаний по модулю json. Есть файл orders
# в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
# его заполнение данными.

# Для этого:
# Создать функцию write_order_to_json(), в которую передается
# 5 параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать запись
# данных в виде словаря в файл orders.json. При записи данных указать
# величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json()
# с передачей в нее значений каждого параметра.

# ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
# ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

# {
#     "orders": []
# }

# вам нужно подгрузить JSON-объект
# и достучаться до списка, который и нужно пополнять
# а потом сохранять все в файл

import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open("orders.json") as f_n:
        dictToJson = json.load(f_n) # переводим в Пайтон словарь
        print(dictToJson)
        dictToJson["orders"].append({"item": item, "quantity": quantity,
            "price": price, "buyer": buyer, "date": date}) # дополняем словарь
    
    with open("orders.json", "w") as f_j:
        json.dump(dictToJson, f_j, indent=2) # переводим список в json объект с отступом 4


write_order_to_json("Toys", 1000, 500, "Canon Group", "01.01.2023")
write_order_to_json("Books", 5000, 50, "Big TV", "01.02.2023")                    
write_order_to_json("Plates", 6000, 100, "Telecom", "01.03.2023")
write_order_to_json("Forks", 7000, 70, "Zandz", "01.04.2023")
write_order_to_json("Spoons", 8000, 40, "AMK Group", "01.05.2023")
write_order_to_json("Plates", 9000, 20, "Panasonic", "01.06.2023")

    