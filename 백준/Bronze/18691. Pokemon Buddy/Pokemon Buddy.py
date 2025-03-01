t = int(input())
for _ in range(t):
    g, c, e = map(int, input().split())
    print(max(0, (e - c) * [1, 3, 5][g - 1]))
