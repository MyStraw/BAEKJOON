N = int(input())
arr = list(map(int, input().split()))

min_value = arr[0]
best = 0
answer = [0]

for i in range(1, N):
    best = max(best, arr[i] - min_value)
    min_value = min(min_value, arr[i])
    answer.append(best)

print(*answer)