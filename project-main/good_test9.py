ls = [0]
i = int(input())
l = list(map(int, input().split()))
a, b = map(int, input().split())
c = 0
for i in l:
	c += i
	ls.append(c)
print(ls[b]-ls[a-1])

