ls = {1: 1, 2: 1}
def fib(n):
	if n not in ls.keys():
		ls[n] = fib(n-1) + fib(n-2)
	return ls[n]
print(fib(int(input())))
