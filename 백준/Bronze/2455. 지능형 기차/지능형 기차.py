cur = 0
mx = 0

for _ in range(4):
    off, on = map(int, input().split())
    cur -= off
    cur += on
    if cur > mx:
        mx = cur

print(mx)