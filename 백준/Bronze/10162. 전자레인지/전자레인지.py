T = int(input())

A = 300
B = 60
C = 10

if T % 10 != 0:
    print(-1)
else:
    a = T // A
    T %= A
    b = T // B
    T %= B
    c = T // C
    print(a, b, c)