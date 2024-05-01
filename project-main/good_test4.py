a, b = map(int, input().split())
c = 0
for i in range(1, a + 1):
	if i%b == 0:
		c+=1
print(c)
