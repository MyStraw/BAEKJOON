T = int(input())

LIMIT_CACHE = 2000000
memo = {1: 1}

out = []
for _ in range(T):
    n = int(input())
    x = n
    path = []

    while True:
        if x == 1:
            base = 1
            break
        if x <= LIMIT_CACHE and x in memo:
            base = memo[x]
            break
        path.append(x)
        if x % 2 == 0:
            x //= 2
        else:
            x = x * 3 + 1

    cur = base
    for v in reversed(path):
        if v > cur:
            cur = v
        if v <= LIMIT_CACHE:
            memo[v] = cur

    out.append(str(cur))

print("\n".join(out))
