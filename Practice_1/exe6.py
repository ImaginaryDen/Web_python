from typing import ForwardRef


def cache_func(n):
	def	cache(f):
		memo = dict()
		def func():
			if any(memo) == False or memo['count'] == n:
				memo["cache"] = f()
				memo["count"] = 1
				print("use")
			else:
				memo["count"] = memo["count"] + 1
			return memo["cache"]
		return func
	return cache

@cache_func(n = 10)
def	get_num():
	return (123)


for i in range(1, 10):
	get_num()