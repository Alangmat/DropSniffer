import json
import os
import mailing
import items
import matplotlib.pyplot as plt

def printDrop(flag):
    # Путь к JSON файлу
    json_file_path = 'spring_drops_count.json'
    # json_file_path = 'merman_drops_count.json'

    # Загрузка словаря из JSON файла или создание нового, если файл отсутствует
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            try:
                drops_count = json.load(f)
            except:
                drops_count = {}
    else:
        drops_count = {}

    cat_flag = flag

    sm = sum(drops_count.values())
    sorted_dict = dict(sorted(drops_count.items(), key=lambda item: item[1], reverse=True))

    if cat_flag:
        # print(sorted_dict)
        drops = {
            "Слитки": 0,
            "Крафтовые ресурсы": 0,
            "Сферы усиления" : 0,
            "Реликвии": 0,
            "Бижутерия 32лвл" : 0,
            "Бижутерия 34лвл": 0,
            "Расходники": 0,
            "Костюмы": 0,
            "Синие пухи 32лвл": 0,
            "Синие пухи 34лвл": 0,
            "Фиолетовые пухи 32лвл": 0,
            "Фиолетовые пухи 34лвл": 0,
            "Баги": 0,
        }

        for key in sorted_dict.keys():
            if key in items.bars.keys():
                drops["Слитки"] += sorted_dict[key]
            elif key in items.crafting_resourses.keys():
                drops["Крафтовые ресурсы"] += sorted_dict[key]
            elif key in items.amplification.keys():
                drops["Сферы усиления"] += sorted_dict[key]
            elif key in items.great_relics.keys():
                drops["Реликвии"] += sorted_dict[key]
            elif key in items.spring_accessories_32.keys():
                drops["Бижутерия 32лвл"] += sorted_dict[key]
            elif key in items.spring_accessories_34.keys():
                drops["Бижутерия 34лвл"] += sorted_dict[key]
            elif key in items.spring_consumables_32.keys():
                drops["Расходники"] += sorted_dict[key]
            elif key in items.spring_costumes.keys():
                drops["Костюмы"] += sorted_dict[key]
            elif key in items.spring_weapons_32_rare.keys():
                drops["Синие пухи 32лвл"] += sorted_dict[key]
            elif key in items.spring_weapons_34_rare.keys():
                drops["Синие пухи 34лвл"] += sorted_dict[key]
            elif key in items.spring_weapons_32_unique.keys():
                drops["Фиолетовые пухи 32лвл"] += sorted_dict[key]
            elif key in items.spring_weapons_34_unique.keys():
                drops["Фиолетовые пухи 34лвл"] += sorted_dict[key]
            else: 
                drops["Баги"] += sorted_dict[key]
        # print(drops)

        sorted_drops = dict(sorted(drops.items(), key=lambda item: item[1], reverse=True))

        labels = sorted_drops.keys()
        values = [x/sm * 100 for x in sorted_drops.values()]


    else:
        dict_str_byte_drop = {}
        for key in items.drops.keys() :
            key_parse = mailing.parse_packet(key)
            str_key = "".join(key_parse[2:len(key_parse)])
            dict_str_byte_drop[str_key] = items.drops[key]


        values = [x/sm * 100 for x in sorted_dict.values()]
        labels = []
        for x in sorted_dict.keys():
            if x in items.spring_data:labels.append(items.spring_data[x])
            # if x in items.merman_data:labels.append(items.merman_data[x])
            # if x in dict_str_byte_drop.keys(): labels.append(dict_str_byte_drop[x])
            else: labels.append(x)

        # print(labels)

    plt.figure(figsize=(18, 10))  # Размер фигуры
        # plt.bar(labels, values, color=plt.cm.tab20.colors)  # Столбчатая диаграмма

    bars = plt.bar(labels, values, color=plt.cm.tab20.colors)  # Столбчатая диаграмма

        # Добавление подписей значений над каждым столбиком
    for bar in bars:
        height = bar.get_height()  # Высота столбика
        plt.text(
            bar.get_x() + bar.get_width() / 2,  # Координата X текста (центр столбика)
            height + 0.5,  # Координата Y текста (чуть выше столбика)
            f'{height:.1f}',  # Текст подписи с одним знаком после запятой
            ha='center',  # Горизонтальное выравнивание
            va='bottom',  # Вертикальное выравнивание
            fontsize=8  # Размер шрифта
        )

    plt.yticks(range(0,80 if cat_flag else 30))
    plt.title(f'Распределение значений, кол-во записей: {sm}', fontsize=14)  # Заголовок
    plt.xlabel("Дроп", fontsize=12)  # Подпись оси X
    plt.ylabel("Вероятность дропа, %", fontsize=12)  # Подпись оси Y
    plt.xticks(rotation=45, ha="right")  # Поворот меток оси X
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Сетка только для оси Y

    plt.tight_layout()  # Уменьшение пустого пространства
    plt.show()  







