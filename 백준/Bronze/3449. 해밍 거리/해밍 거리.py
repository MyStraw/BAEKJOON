t = int(input())
for _ in range(t):
    a = input().strip()
    b = input().strip()
    distance = sum(x != y for x, y in zip(a, b))
    print(f"Hamming distance is {distance}.")
