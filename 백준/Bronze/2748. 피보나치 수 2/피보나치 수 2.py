n = int(input())

if n == 0:
    print(0)
else:
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    print(a)