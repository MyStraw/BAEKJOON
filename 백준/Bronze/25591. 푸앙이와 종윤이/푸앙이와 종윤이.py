x, y = map(int, input().split())

a = 100 - x
b = 100 - y
c = 100 - (a + b)
d = a * b
q = d // 100
r = d % 100

print(a, b, c, d, q, r)

front = c + q
back = r

def fmt(v):
    if v >= 0 and v < 10:
        return str(v)
    return str(v)

print(fmt(front), fmt(back))
