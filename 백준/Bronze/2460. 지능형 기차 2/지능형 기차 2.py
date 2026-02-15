cur = 0
mx = 0

for _ in range(10):
    off, on = map(int, input().split())
    cur = cur - off + on
    if cur > mx:
        mx = cur

print(mx)