def root(A, n = 2):
    if n==0:
        return 0
    x=A/n
    while True:
        x_1 = ((n-1) * x + A / pow(x, n-1))/n
        if abs(x-x_1)>0.00001:
            x=x_1
        else:
            break
    return x_1

while(1):
	try:
		print (root(int(input("input number\n")), int(input("input degree\n"))))
	except:
		break