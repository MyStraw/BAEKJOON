n = int(input().strip())
ans = None
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        if ans is None or b < ans:
            ans = b
print(-1 if ans is None else ans)
