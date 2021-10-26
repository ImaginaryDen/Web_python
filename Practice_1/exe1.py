def is_palin(num):
	if num < 0:
		num = - num
	return (str(num) == str(num)[::-1])

while(1):
	try:
		print(is_palin(int(input("input number\n"))))
	except:
		break