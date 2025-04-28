n, m = map(int, input().split())
count = 0
for _ in range(n):
    row = input()
    if '+' in row:
        count += 1
print(count)
