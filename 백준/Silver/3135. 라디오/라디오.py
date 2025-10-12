A, B = map(int, input().split())
N = int(input())
presets = [int(input()) for _ in range(N)]
ans = abs(A - B)
for f in presets:
    ans = min(ans, 1 + abs(f - B))
print(ans)
