import sys

input = sys.stdin.readline

n = int(input().strip())

best_x = None
best_y = None

for _ in range(n):
    x, y = map(int, input().split())
    if best_y is None or y < best_y or (y == best_y and x < best_x):
        best_x, best_y = x, y

print(best_x, best_y)
