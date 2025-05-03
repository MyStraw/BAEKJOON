x, y = map(int, input().split())

for t in range(0, 10000):
    cycle = t % (2 * x)   
    if cycle == (y + x) % (2 * x):
        print(t)
        break
