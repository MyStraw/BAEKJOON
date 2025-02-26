N, M = map(int, input().split())

for i in range(N):
    print(" ".join(map(str, range(i * M + 1, (i + 1) * M + 1))))