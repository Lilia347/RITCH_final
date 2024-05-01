n = int(input())
ls = [int(i) for i in input().split()]
l, r = map(int, input().split())
ls.sort()
print(ls[r-1] - ls[l-1])