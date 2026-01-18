N, X, K = map(int, input().split())

pos = X
for _ in range(K):
    a, b = map(int, input().split())
    if pos == a:
        pos = b
    elif pos == b:
        pos = a

print(pos)
