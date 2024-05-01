a = int(input())
c = 0
b = list(map(int, input().split()))
for i in b:
	c = c^i
print(2 if c == 0 else 1)