import math
c, cc = 10**6, 10 ** 5 * 1.32
cc = int(cc)
res = math.gcd(c, cc)
print(res, int(c * cc / res))