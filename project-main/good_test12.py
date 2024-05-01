import math
k = int(input())
glb = 0
for n in range(len(str(k)) - 1):
    cnt = 0
    for i in range(10 ** n, 10 ** n + n + 1):
        if math.gcd(i, n + 1) == 1 or n + 1 == 1:
            cnt+=1
    f = 9 * 10**n % (n+1)
    if f > 0:
        cnt *= (9 * 10**n - 1) // (n+1)
        for i in range(10**(n+1) - f, 10**(n+1)):
            if math.gcd(i, n + 1) == 1 or n + 1 == 1:
                cnt+=1
    else:
        cnt *= (9 * 10**n)//(n+1)
    glb += int(cnt)
 
nc = k - 10 ** (len(str(k)) - 1)
n = len(str(k))
cnt = 0
sz  =  k - 10 ** (n - 1) + 1
f = (sz) % (n)
for i in range(10 ** (n - 1), 10 ** (n - 1) + n):
    if math.gcd(i, n) == 1 or n == 1:
        cnt+=1
if f > 0:
    cnt *= (sz) // (n)
    for i in range(k - f + 1, k + 1):
        if math.gcd(i, n) == 1 or n == 1:
            cnt+=1
else:
    cnt *= (sz)//(n)
 
print(int(cnt + glb))
