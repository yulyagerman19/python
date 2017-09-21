#простые числа
print('Вывод всех простых чисел')
print('Введите число')
	a = input('a= ')
	lst=[]
	for i in xrange(2, a+1):
    
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print lst
