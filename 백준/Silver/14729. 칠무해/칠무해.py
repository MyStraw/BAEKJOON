import sys
input = sys.stdin.readline

N = int(input())

count = [0] * 100001

for _ in range(N):
    x = input().strip()
    idx = int(float(x) * 1000)
    count[idx] += 1

printed = 0

for i in range(100001):
    while count[i] > 0:
        print(f"{i/1000:.3f}")
        count[i] -= 1
        printed += 1
        if printed == 7:
            exit()