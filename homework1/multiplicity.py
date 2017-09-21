#кратность 5
print('Вывод всех кратных 5 чисел между a и b')
print('Введите число a')
	a = int(input('a =  '))
print('Введите число b')
	b = int(input('b =  '))
			
	list = []
	  
	for i in range (a, b+1):
		if i % 5 == 0:
		
		list.append(i)

print list