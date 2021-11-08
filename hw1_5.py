revenue = int(input('Выручка Вашей фирмы - '))
loss = int(input('Издержки Вашей фирмы - '))
profit = revenue - loss
if revenue == loss:
	print('Вы работаете в 0')
elif revenue > loss:
	print(f'Поздравляем! Вы работаете с прибылью. Рентабельность выручки - {profit/revenue}')
	staff = int(input('Введите количество сотрудников фирмы - '))
	print(f'Прибыль фирмы в расчете на одного сотрудника - {"{:.2f}".format(profit / staff)}')
else:
	print('К сожалению, Ваша фирма работает в убыток =(')
