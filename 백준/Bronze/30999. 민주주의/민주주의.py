N, M = map(int, input().split())
need = M // 2 + 1
ans = 0
for _ in range(N):
    s = input().strip()
    if s.count('O') >= need:
        ans += 1
print(ans)
