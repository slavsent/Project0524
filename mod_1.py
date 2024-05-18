'''
# Задание 1
# имеется текстовый файл f.csv, по формату похожий на .csv с разделителем |
"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одинаковым id присутствуют разные данные - собрать такие записи
'''


def data_in_file(file_name):
    with open(file_name, "r", encoding='utf') as file:
        i = 0
        num = 1
        res = {}
        for line in file:
            if i == 0:
                list_name = line[:-1].split('|')

                try:
                    id_num = list_name.index('id')
                except Exception:
                    id_num = len(list_name)
            else:
                if '\n' in line:
                    list_data = line[:-1].split('|')
                else:
                    list_data = line.split('|')
                if list_data[id_num] not in res.keys():
                    res[list_data[id_num]] = {}
                    for j in range(len(list_data)):
                        if j == id_num:
                            continue
                        res[list_data[id_num]][list_name[j]] = list_data[j]
                else:
                    new_dict = {}
                    for j in range(len(list_data)):
                        if j == id_num:
                            continue
                        new_dict[list_name[j]] = list_data[j]
                    if new_dict != res[list_data[id_num]]:
                        res[f'{list_data[id_num]}_{num}'] = new_dict
                        num += 1
            i += 1
    return res


if __name__ == '__main__':
    print(data_in_file('f.csv'))
