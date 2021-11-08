time = int(input('Введите время в секундах:'))
hours = time // 3600
minute = time % 3600 // 60
sec = time % 3600 % 60
print(f'{hours} : {minute:02} : {sec:02}')
