T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    total = 0
    for c in candies:
        total += c // K
    print(total)
