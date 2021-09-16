def is_palin(num):
	return (str(num) == str(num)[::-1])

print(is_palin(121))
