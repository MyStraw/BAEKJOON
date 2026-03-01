x, y = map(int, input().split())
n = int(input())

best = x / y

for _ in range(n):
    xi, yi = map(int, input().split())
    price_per_g = xi / yi
    if price_per_g < best:
        best = price_per_g

ans = best * 1000
print(f"{ans:.2f}")