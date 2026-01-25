a, b = map(int, input().split())
c, d = map(int, input().split())

num = a * d + b * c
den = b * d

x, y = num, den
while y:
    x, y = y, x % y
g = x

print(num // g, den // g)
