t = int(input())
out = []

for _ in range(t):
    x = int(input())

    if x == 0 or x == 1:
        out.append("1")
    else:
        a = 1
        b = 1
        for _ in range(2, x + 1):
            a, b = b, a + b
        out.append(str(b))

print("\n".join(out))