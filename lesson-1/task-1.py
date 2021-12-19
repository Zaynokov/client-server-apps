words = ['разработка', 'сокет', 'декоратор']

print('До преобразования')
[print(type(word)) for word in words]
[print(word) for word in words]

unicode_words = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

print('\nПосле преобразования')
[print(type(word)) for word in unicode_words]
[print(word) for word in unicode_words]

