import sys

input = sys.stdin.readline

N = int(input().strip())
ans = ""
for _ in range(N):
    name, year = input().split()
    if int(year) == 2026:
        ans = name

print(ans)
