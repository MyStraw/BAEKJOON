N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

total_sum = sum(A)
answer = 0

for num in A:
    total_sum -= num
    answer = (answer + num * total_sum) % MOD

print(answer)