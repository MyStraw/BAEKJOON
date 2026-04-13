N, W, H = map(int, input().split())

limit = (W * W + H * H) **0.5

for _ in range(N):
    length = int(input())
    if length <=limit:
        print("DA")
    else:
        print("NE")