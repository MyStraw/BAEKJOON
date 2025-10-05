N = int(input())
A = [int(input()) for _ in range(N)]
M = int(input())
total = 0
for _ in range(M):
    B = int(input())
    total += A[B-1]
print(total)