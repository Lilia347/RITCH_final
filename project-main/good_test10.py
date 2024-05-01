a, b = map(int, input().split())
ls = [[int(i) for i in input().split()] for _ in range(b)]
ls1 = [[0 for _ in range(a)] for _ in range(b)]
ls1[0][0] = ls[0][0]
for i in range(1, a):
    ls1[0][i] = ls1[0][i-1] + ls[0][i]
for i in range(1, b):
    ls1[i][0] = ls1[i-1][0] + ls[i][0]
for i in range(1, b):
    for j in range(1, a):
        ls1[i][j] = max(ls1[i][j-1], ls1[i-1][j]) + ls[i][j]
print(ls[-1][-1])