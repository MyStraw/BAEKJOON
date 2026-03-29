N = int(input())

t = [0] * (N + 1)
p = [0] * (N + 1)

for i in range(1, N + 1):
    ti, pi = map(int, input().split())
    t[i] = ti
    p[i] = pi

dp = [0] * (N + 2)

for i in range(N, 0, -1):
    if i + t[i] <= N + 1:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else:
        dp[i] = dp[i + 1]

print(dp[1])