def my_sqrt(num):
	for i in range(1, num - 1):
		res = ((i**2 + num) / i) / 2
		#print (res)
		if (round(res ** 2) == num):
			return (res)
print(my_sqrt(16))