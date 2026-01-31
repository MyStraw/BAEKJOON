N = int(input())

prev = int(input())
diffs_g = 0
diffs = []

for _ in range(N - 1):
    cur = int(input())
    d = cur - prev
    diffs.append(d)
    if diffs_g == 0:
        diffs_g = d
    else:
        a, b = diffs_g, d
        while b:
            a, b = b, a % b
        diffs_g = a
    prev = cur

ans = 0
g = diffs_g
for d in diffs:
    ans += d // g - 1

print(ans)
