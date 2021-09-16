def	prime(num):
	for i in range(2, int(num / 2) + 1):
		if	(num % i == 0 and i != num):
			return (False)
	return(True)
print(prime(11))