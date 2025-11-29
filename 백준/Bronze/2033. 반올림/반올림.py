N = int(input())

place = 1
while place <= N:
    if N > place * 10:
        N = (N + place * 5) // (place * 10) * (place * 10)
    place *= 10

print(N)
