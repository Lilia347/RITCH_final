from math import sqrt
c = float(input())
left = 0
right = 1e10
while right - left > 10e-10:
    middle = (left + right) / 2
    if middle * middle + sqrt(middle) >= c:
        right = middle
    else:
        left = middle
print(int(round(left*10e6))/10e6)
