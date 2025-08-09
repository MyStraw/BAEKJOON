import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sum(1 for a, b in zip(A, B) if b >= a))
