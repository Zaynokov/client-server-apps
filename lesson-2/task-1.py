import csv

files = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for f in files:
        with open(f) as file:
            file_reader = csv.reader(file)
            for row in file_reader:
                data = row[0].split(':')
                if len(data) >= 2:
                    key, item = data[0], data[1].strip()
                if key == 'Изготовитель системы':
                    os_prod_list.append(item)
                elif key == 'Название ОС':
                    os_name_list.append(item)
                elif key == 'Код продукта':
                    os_code_list.append(item)
                elif key == 'Тип системы':
                    os_type_list.append(item)

    for i in range(3):
        main_data.append([
            os_prod_list[i],
            os_name_list[i],
            os_code_list[i],
            os_type_list[i],
        ])
    return main_data


def write_to_csv(file):
    with open(file, 'w', encoding='utf-8') as csv_file:
        file_writer = csv.writer(csv_file)
        for row in get_data():
            file_writer.writerow(row)


write_to_csv('new.csv')
