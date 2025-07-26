shu_map = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}
n = int(input())
total = 0

for _ in range(n):
    pepper = input().strip()
    total += shu_map[pepper]

print(total)
