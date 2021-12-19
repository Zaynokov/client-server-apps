words = ['разработка', 'администрирование', 'protocol', 'standard']

encode_words = [word.encode('utf-8') for word in words]
print(*encode_words, sep='\n', end='\n\n')


[print(word.decode('utf-8')) for word in encode_words]
