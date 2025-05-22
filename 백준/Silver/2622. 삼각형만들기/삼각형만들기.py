n = int(input())
count = 0

for a in range(1, n // 3 + 1):
    b_start = max(a, n // 2 - a + 1)
    b_end = (n - a) // 2
    if b_end >= b_start:
        count += (b_end - b_start + 1)

print(count)
