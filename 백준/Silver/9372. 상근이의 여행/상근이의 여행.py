T = int(input())
out = []

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        input()
    out.append(str(N - 1))

print("\n".join(out))