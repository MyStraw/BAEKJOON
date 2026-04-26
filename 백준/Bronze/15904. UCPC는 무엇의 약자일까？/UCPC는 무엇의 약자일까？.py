s = input()

target = "UCPC"
idx = 0

for ch in s:
    if ch == target[idx]:
        idx += 1
        if idx == 4:
            break

if idx == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")