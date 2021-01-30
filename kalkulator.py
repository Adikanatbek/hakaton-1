while True:
	#if a in ('*', '/','-','+'):
	num = float(input('первое число: '))
	num2 = float(input("второе число: "))
	a = (input('Выберите знак, (*,/,+,-): '))
	if a ==  "+":
		result = num + num2
		
	elif a == "-":
		result = num - num2
		
	elif a == "*":
		result = num * num2
		
	elif a == "/":
		result = num / num2	


	print(result)

