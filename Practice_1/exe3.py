def rev(num):
	if num < 0:
		return int(str(-num)[::-1]) * -1
	return int(str(num)[::-1])

while(1):
	try:
		print(rev(int(input("input number\n"))))
	except:
		break