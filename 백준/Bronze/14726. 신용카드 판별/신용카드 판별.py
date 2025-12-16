import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    s = input().strip()
    total = 0
    rev = s[::-1]

    for i in range(16):
        d = int(rev[i])
        if i % 2 == 1:
            d *= 2
            if d >= 10:
                d = d // 10 + d % 10
        total += d

    if total % 10 == 0:
        print("T")
    else:
        print("F")
