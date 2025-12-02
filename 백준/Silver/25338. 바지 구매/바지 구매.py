import sys
import math
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
N = int(input())

ans = 0

for _ in range(N):
    u, v = map(int, input().split())

    if u == c:
        x = b
    else:
        x = b + math.sqrt((c - u) / -a)

    if abs(x - v) < 1e-9:
        ans += 1

print(ans)
