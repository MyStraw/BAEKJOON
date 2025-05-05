N = int(input())
A, B, C = map(int, input().split())

result = min(A, N) + min(B, N) + min(C, N)
print(result)
