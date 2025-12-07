import sys

N, M = map(int, sys.stdin.readline().split())

if N == 0:
    print(0)
else:
    print((N + M - 1) // M)
