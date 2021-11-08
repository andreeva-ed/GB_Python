start_km = int(input('Введите результат, который пробежал спортсмен в 1-й день (км) - '))
aim_km = int(input('Введите цель спортсмена (км) - '))
i = 1
while start_km <= aim_km:
    print (f'{i}-й день:{"{:.2f}".format(start_km)}')
    start_km = start_km + start_km * 0.1
    i = i + 1
print (f'{i}-й день:{"{:.2f}".format(start_km)}')
print (f'На {i}-й день спортсмен достиг результата - не менее {aim_km} км')
