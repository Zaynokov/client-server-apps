with open("test_file.txt") as file:
    print(f'Кодировка файла по умолчанию - {file.encoding}', end='\n\n')

with open("test_file.txt", encoding='utf-8') as file:
    print('Содержимое файла:')
    for line in file:
        print(line, end='')

