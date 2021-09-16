def get_three_list(nums):
	list_2 = list()
	list_3 = list()
	list_5 = list()
	for num in nums:
		if ((num % 2) == 0):
			list_2.append(num)
		if ((num % 3) == 0):
			list_3.append(num)
		if ((num % 5) == 0):
			list_5.append(num)
	return (list_2, list_3, list_5)

list_nums = (range(1, 100))
result = get_three_list(list_nums)
print(result[0])
print(result[1])
print(result[2])