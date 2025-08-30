import sys, math

data = list(map(int, sys.stdin.read().strip().split()))
if not data:
    print(0)
    raise SystemExit

n, e = data[0], data[1]
idx = 2

w = sum(data[idx:idx + max(0, n - 1)])
idx += max(0, n - 1)

h = sum(data[idx:idx + max(0, e - 1)])

ans = math.ceil(math.hypot(w, h))
print(ans)
