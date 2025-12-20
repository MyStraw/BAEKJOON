import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x = int(input())
    total = 0.0
    for _ in range(x):
        _, qty, price = input().split()
        total += int(qty) * float(price)
    print(f"${total:.2f}")
