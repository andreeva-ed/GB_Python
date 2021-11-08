# number = input('Введите целое положительное число: ')
# n = list(number)
# print(max(n))

number = int(input('Введите целое положительное число: '))
res = number % 10
number = number // 10
while number > 0:
	if number % 10 > res:
		res = number % 10
	number = number // 10
print(res)
