sz = int(input())
D = [list(map(int, input().split())) for i in range(sz)]
queue = [(0, -1)]
used = [False for _ in range(sz)]
prev = -1
flag = False
while len(queue) and not flag:
    now, prev = map(int, queue.pop(0))
    used[now] = True
    for n, i in enumerate(D[now]):
        if n == now and i == 1:
            print("NO")
            exit()
        if prev != -1 and i != 0 and n != now:
            if used[n] is True and n != prev and i != 0:
                flag = True
                break
        if i != 0 and n != now and  n!=prev:
            queue.append((n, now))
if used.count(True) < sz:
    flag = True
print("NO" if flag else "YES")