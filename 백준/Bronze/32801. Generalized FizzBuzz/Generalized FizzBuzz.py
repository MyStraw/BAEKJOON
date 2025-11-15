import math

n, a, b = map(int, input().split())

l = a * b // math.gcd(a, b)

fb = n // l
f = n // a - fb
bu = n // b - fb

print(f, bu, fb)
