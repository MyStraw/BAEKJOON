n = int(input())
target = list(map(int, input().split()))
state = [0] * n
count = 0

for i in range(n):
    if state[i] != target[i]:
        count += 1
        state[i] ^= 1
        if i + 1 < n:
            state[i+1] ^= 1
        if i + 2 < n:
            state[i+2] ^= 1

print(count)