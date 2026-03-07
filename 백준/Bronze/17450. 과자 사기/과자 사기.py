s_price, s_weight = map(int, input().split())
n_price, n_weight = map(int, input().split())
u_price, u_weight = map(int, input().split())

def value(price, weight):
    total_price = price * 10
    if total_price >= 5000:
        total_price -= 500
    total_weight = weight * 10
    return total_weight / total_price

s = value(s_price, s_weight)
n = value(n_price, n_weight)
u = value(u_price, u_weight)

if s > n and s > u:
    print("S")
elif n > s and n > u:
    print("N")
else:
    print("U")