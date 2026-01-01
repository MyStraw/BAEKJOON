import sys

A, B = map(int, sys.stdin.readline().split())
K, X = map(int, sys.stdin.readline().split())

L = max(A, K - X)
R = min(B, K + X)

cnt = R - L + 1
if cnt <= 0:
    print("IMPOSSIBLE")
else:
    print(cnt)
