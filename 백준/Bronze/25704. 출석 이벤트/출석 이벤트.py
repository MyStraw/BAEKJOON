n = int(input())
p = int(input())

discounts = []
if n >= 5:
    discounts.append(p - 500)
if n >= 10:
    discounts.append(int(p * 0.9))
if n >= 15:
    discounts.append(p - 2000)
if n >= 20:
    discounts.append(int(p * 0.75))

discounts.append(p)
print(max(0, min(discounts)))
