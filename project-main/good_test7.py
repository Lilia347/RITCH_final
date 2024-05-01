
stack = []
for i in range(int(input())):
	n = input()
	if n == "clear":
		stack = []
	elif n == "pop":
		try:
			stack.pop()
		except:
			pass
	else:
		stack.append(int(n.split()[1]))
print(stack[-1] if len(stack)>0 else -1)
