N = int(input())
origin = N
cycle = 0

while True:
    ten = N // 10
    one = N % 10
    total = ten + one
    N = (one * 10) + (total % 10)
    cycle += 1
    if N == origin:
        break

print(cycle)