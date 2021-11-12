my_str = input('Введите строку из нескольких слов, разделенных пробелами: ')
for i, word in enumerate(my_str.split(' '), 1):
    if len(word) > 10:
        word = word[:10]
    print(i, word)